from Database import Database
from bson.json_util import dumps

class TaskManager():
    # summarizer = Summarizer()
    # scheduler = Scheduler()
    def __init__(self):
        print("TaskManager Initializing...")
        print("TaskManager - Done!")

    def __del__(self):
        pass

    def summarize_news(self):
        summary = "This is News Summary"
        return summary

    def get_latest_news(self):
        client = Database.getInstance()
        db = client.get_database("headline")
        collection = db.get_collection("news")
        documents = dumps(collection.find().sort("date",-1).limit(30), ensure_ascii=False)
        return documents

    def get_news_by_category(self, category, limit):
        client = Database.getInstance()
        db = client.get_database("headline")
        collection = db.get_collection("news")
        query = {"category": category}
        documents = dumps(collection.find(query).sort("date",-1).limit(limit), ensure_ascii=False)

        return documents