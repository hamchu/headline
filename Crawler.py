from Database import Database
from bs4 import BeautifulSoup
import Utils
import requests

class Crawler():
    __base_url = "https://news.nate.com/view/"

    def __init__(self):
        print("Crawler Initializing...")
        print("Crawler - Done!")

    def __del__(self):
        pass

    def crawl(self):
        print("crawling...")

        # TODO : 크롤링 처리 범위 해결해야함.
        for x in range(10000, 10100):
            additional_url = '{0:05d}'.format(x)
            page_url = self.__base_url + str(20201004) + "n" + additional_url
            self.parse_page(page_url)

        print("crawling done!")

    def parse_page(self, source_url):
        req = requests.get(source_url)
        if (req.request.url[8:14] == "sports"): return  # sports 뉴스면 return

        print("now : " + str(req.request.url))
        html = req.content
        soup = BeautifulSoup(html, 'lxml', None, None, "CP949")
        if (soup.find('span', class_='firstDate') == None): return
        if (soup.find('h3', class_='articleSubecjt') == None): return

        # 해외뉴스 언론사 제외
        if (soup.find('a', class_='medium') != None):
            medium = soup.find('a', class_='medium').getText()
            if (medium == "EPA연합뉴스"): return  # 영어뉴스 임마들 희안하게 긁어오더라...
            if (medium == "AP연합뉴스"): return
        else:
            return

        news_date = soup.find('span', class_='firstDate').find('em').getText()  # 뉴스 날짜
        news_title = soup.find('h3', class_='articleSubecjt').getText()  # 뉴스 제목
        if (soup.find('a', class_='articleOriginal') == None):
            news_original = str(req.request.url)
        else:
            news_original = str(soup.find('a', class_='articleOriginal').get('href'))  # 원문링크

        # TODO : 원문내용 처리
        news_contents = soup.find('div', id='realArtcContents').getText()
        if (len(news_contents) < 30): return  # 짧아도 니 리턴
        if (soup.find('div', id='mediaSubnav') == None):
            category = "연예"
        else:
            category = soup.find('div', id='mediaSubnav').find('a').getText()

        # 임시로 그림없는 기사는 버리는 걸로 해놓음.
        if (soup.find('span', class_='imgad_area') == None): return
        thumbnail_temp = "https:" + str(soup.find('span', class_='imgad_area').find('img').get('src'))
        thumbnail = Utils.encode_image_to_base64string(thumbnail_temp)

        # news_original_firm = soup.find('a', class_='medium').getText()  # 언론사
        news = {
            "category": category,
            "title": news_title,
            "contents": news_contents,
            "thumbnail": thumbnail,
            "original_url": news_original,
            "date": news_date,
        }

        client = Database.getInstance()
        db = client.get_database("headline")
        collection = db.get_collection("news")
        collection.insert_one(news)
