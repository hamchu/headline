from Crawler import Crawler
from flask import Flask, request, jsonify
import json

class Server:
        def __init__(self, taskmanager):
                self.app = Flask(__name__)
                self.tm = taskmanager
                print("Initialize Server...")

                @self.app.route("/", methods=["GET"])
                def is_server_available():
                        return jsonify({
                                "result": "HeadLine Server On"
                        })

                @self.app.route("/summary", methods=["GET"])
                def summarize_news():
                        text = request.args.get("text")
                        summary = self.tm.summarize_news(text)

                        return json.dumps({
                                "summary": summary
                        }, ensure_ascii=False)

                @self.app.route("/home", methods=["GET"])
                def get_latest_news():
                        news_list = json.loads(self.tm.get_latest_news())
                        return json.dumps(news_list, ensure_ascii=False)

                @self.app.route("/news", methods=["GET"])
                def get_news_by_category():
                        category = request.args.get("cate")
                        limit = int(request.args.get("limit"))
                        news_list = json.loads(self.tm.get_news_by_category(category, limit))
                        return json.dumps(news_list, ensure_ascii=False)

                @self.app.route("/crawling", methods=["GET"])
                def crawling():
                        category = request.args.get("category")
                        date = int(request.args.get("date"))
                        crawler = Crawler()
                        crawler.crawl(category,date)
                        return jsonify({
                                "result": "Crawling Finished!"
                       })

        def run(self, host, port):
                print("Server On")
                self.app.run(host=host,port=port,debug='on')