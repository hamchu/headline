from Crawler import Crawler
from flask import Flask, request, jsonify
import json

class Server:
        def __init__(self, taskmanager):
                self.__app = Flask(__name__)
                self.__tm = taskmanager
                self.__crawler = Crawler() # 임시

                @self.__app.route("/", methods=["GET"])
                def is_server_available():
                        return jsonify({
                                "result": "HeadLine Server On"
                        })

                @self.__app.route("/summary", methods=["GET"])
                def summarize_news():
                        text = request.args.get("text")
                        # summary = self.__tm.summarize_news(text)

                        return json.dumps({
                                # "summary": summary
                                "summary": "Test중... 뉴스에 대한 요약본을 제공하여 사용자로 하여금 정보를 더욱 빠르고 간결하게 얻을 수 있게 해드리겠습니다. 고양예술은행은 고양문화재단이 주최-주관해 코로나19 경제난을 겼는 지역 예술인에게 창작 공모사업을 통해 우수한 예술창작물을 선정해 상금을 지원하는 전국 최초의 은행제도 사업이다.  이번 공모는 9월24일부터 10월12일까지 19일간 공연 시각 전통 공감 등 4개 분야로 공모해 총 275건의 작품이 접수됐다. 이 중 외부전문가로 구성된 심사위원회를 열어 200건을 선정했다. 특히 70세의 최고령 지역예술인의 응모작이 선정됐다.  이재준 고양시장은 “참신한 아이디어로 공모에 선정된 분들에게 축하를 드린다”며 “예술이 코로나19가 남긴 마음의 후유증을 치유하고 보듬으며 우리를 일상으로 돌아가게 하는 강력한 치유제로 작용하기를 기대한다”고 말했다. "
                        }, ensure_ascii=False)

                @self.__app.route("/home", methods=["GET"])
                def get_latest_news():
                        news_list = json.loads(self.__tm.get_latest_news())
                        return json.dumps(news_list, ensure_ascii=False)

                @self.__app.route("/news", methods=["GET"])
                def get_news_by_category():
                        category = request.args.get("cate")
                        limit = int(request.args.get("limit"))
                        news_list = json.loads(self.__tm.get_news_by_category(category, limit))
                        return json.dumps(news_list, ensure_ascii=False)

                @self.__app.route("/crawling", methods=["GET"])
                def crawling():
                        category = request.args.get("category")
                        date = int(request.args.get("date"))

                        self.__crawler.crawl(category,date)
                        return jsonify({
                                "result": "Crawling Finished!"
                       })

        def run(self, host, port):
                print("Server On")
                self.__app.run(host=host,port=port,debug=False)