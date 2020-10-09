from gensim import models
from nltk import sent_tokenize, word_tokenize

class SentenceProcessor():

    def __init__(self):
        print("Load FastText Model...")
        self.fasttext_model = models.fasttext.load_facebook_model('fasttext/cc.ko.300.bin')  # 300차원
        print("Load FastText Model - Done!")

    def tokenize_sentence(self, sentences):
        tokenized_sentences = sent_tokenize(sentences);
        return [word_tokenize(sentence) for sentence in tokenized_sentences]