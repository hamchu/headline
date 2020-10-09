from gensim import models

class SentenceProcessor():

    def __init__(self):
        print("Load FastText Model...")
        self.fasttext_model = models.fasttext.load_facebook_model('fasttext/cc.ko.300.bin')  # 300차원
        print("Load FastText Model - Done!")