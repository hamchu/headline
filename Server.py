from flask import Flask, request, jsonify

class Server:
        def __init__(self):
                self.app = Flask(__name__)
                print("Initialize Server...")

                @self.app.route("/", methods=["GET"])
                def is_server_available():
                        return jsonify({
                                "result": "HeadLine Server On"
                        })

                @self.app.route("/summary", methods=["GET"])
                def summarize_news():
                        summary = self.tm.summarize_news()

                        return jsonify({
                                "result": summary
                        })

                @self.app.route("/home", methods=["GET"])
                def get_latest_news():
                        # latest_news_list = json.loads(self.tm.get_latest_news())
                        return jsonify({
                                "result": "This is home"
                        })

                @self.app.route("/news", methods=["GET"])
                def get_news_by_category():
                        category = request.args.get("cate")
                        limit = int(request.args.get("limit"))
                        # parsed = json.loads(self.tm.get_news_by_category(category, limit))
                        return jsonify({
                                "result": "This is category news"
                        })
                @self.app.route("/crawling", methods=["GET"])
                def crawling():

                        return jsonify({
                                "result": "크롤링 테스트"
                        })

        def run(self, host, port):
                print("Server On")
                self.app.run(host=host,port=port,debug='on')