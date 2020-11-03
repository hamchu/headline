from Database import Database
from bs4 import BeautifulSoup
import Utils, requests, re, time

class Crawler():
    __base_url = "https://news.daum.net/breakingnews/"

    def __init__(self):
        print("Crawler initializing - Done!")

    def crawl(self, category, date):
        print("crawling...")
        page = 1
        while True:
            page_url = self.__base_url + str(category) +'?page=' + str(page) + '&regDate=' + str(date)
            print("nownownownow : "+ page_url)
            req = requests.get(page_url)
            html = req.content
            soup = BeautifulSoup(html, 'lxml')

            if (soup.find('p', class_="txt_none") != None): break;

            list = soup.find('ul', class_="list_news2 list_allnews")
            targets = list.find_all('a', class_='link_thumb')
            for i in range(len(targets)):
                target_url = targets[i].get('href')
                self.parse_page(target_url)

            if(page%2 == 0): time.sleep(12)
            page += 1

        print("crawling done!")

    def parse_page(self, source_url):
        req = requests.get(source_url)

        print("now : " + str(req.request.url))
        html = req.content
        soup = BeautifulSoup(html, 'lxml')
        if (soup.find('span', class_='num_date') == None): return # 날짜가 없으면 return
        if (soup.find('h3', class_='tit_view') == None): return # 기사 제목이 없으면 return

        news_date = soup.find('span', class_='num_date').getText()  # 뉴스 날짜
        news_title = soup.find('h3', class_='tit_view').getText()  # 뉴스 제목

        news_original = str(req.request.url)

        news_contents = str(soup.find_all('p', attrs={'dmcf-ptype': 'general'}))
        news_contents = re.sub('<.+?>', '', news_contents, 0).replace('[', '').replace(']', '').replace(',', '')

        if (len(news_contents) < 30): return  # 기사 내용이 30자 보다 작으면 return

        if (soup.find('div', class_='inner_gnb') == None):
            category = "미분류"
        else:
            category = soup.find('div', id='kakaoContent').find('h2').getText()

        # 임시로 그림없는 기사는 버리는 걸로 해놓음.
        if (soup.find('p', class_='link_figure') == None): return

        thumbnail_temp = str(soup.find('p', class_='link_figure').find('img').get('src'))
        thumbnail = Utils.encode_image_to_base64string(thumbnail_temp)

        news = {
            "category": category,
            "title": news_title,
            "contents": news_contents,
            "thumbnail": thumbnail,
            "source_url": source_url,
            "date": news_date,
        }

        client = Database.getInstance()
        db = client.get_database("headline")
        collection = db.get_collection("news")
        collection.insert_one(news)