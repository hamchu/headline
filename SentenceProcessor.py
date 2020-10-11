from gensim import models
from nltk import sent_tokenize, word_tokenize
import pandas as pd

class SentenceProcessor():

    def __init__(self):
        print("Load FastText Model...")
        self.fasttext_model = models.fasttext.load_facebook_model('fasttext/cc.ko.300.bin')  # 300차원
        print("Load FastText Model - Done!")

        print("Load stop_words.csv...")
        self.stop_words = sum(pd.read_csv("data/stop_words.csv").values.tolist(),[])
        print("Load stop_words - Done!")

    def tokenize_sentence(self, sentences):
        tokenized_sentences = sent_tokenize(sentences)

        return [word_tokenize(sentence) for sentence in tokenized_sentences]

    def preprocess_sentence(self, sentences):
        preprocessed_sentences = []

        for sentence in sentences:
            temp = [word for word in sentence if word not in self.stop_words and word]
            preprocessed_sentences.append(temp)

        return preprocessed_sentences

    def embed_sentence(self, sentences):
        embedded_sentences = []

        for sentence in sentences:
            temp = sum([self.fasttext_model.wv.__getitem__(word) for word in sentence]) / len(sentence)
            embedded_sentences.append(temp)

        return embedded_sentences