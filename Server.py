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
                        summary = self.__tm.summarize_news(text)

                        return json.dumps({
                                "summary": summary
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