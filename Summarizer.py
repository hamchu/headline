from SentenceProcessor import SentenceProcessor
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import networkx as nx

class Summarizer():
    def __init__(self):
        self.__sentence_processor = SentenceProcessor()
        print("Summarizer initializing - Done!")

    def calculate_similarity_matrix(self, embedded_sentences):
        similarity_matrix = np.zeros([len(embedded_sentences), len(embedded_sentences)])

        for i in range(len(embedded_sentences)):
            for j in range(i+1, len(embedded_sentences)):
                similarity_matrix[i][j] = cosine_similarity(embedded_sentences[i].reshape(1, 300),
                                                  embedded_sentences[j].reshape(1, 300))[0, 0]
                similarity_matrix[j][i] = similarity_matrix[i][j]

        return similarity_matrix

    def get_score(self, similarity_matrix):
        nx_graph = nx.from_numpy_array(similarity_matrix)
        scores = nx.pagerank(nx_graph)
        return scores

    def summarize(self, text):
        tokenized_sentences = self.__sentence_processor.tokenize_sentence(text)
        preprocessed_sentences = self.__sentence_processor.preprocess_sentence(tokenized_sentences)
        embedded_sentences = self.__sentence_processor.embed_sentence(preprocessed_sentences)
        similarity_matrix = self.calculate_similarity_matrix(embedded_sentences)
        scores = self.get_score(similarity_matrix)

        score_ranking_list = sorted(((scores[i], s) for i, s in enumerate(self.__sentence_processor.get_tokenized_sentences(text))),
                            reverse=True)
        top_sentences = [sentence for score, sentence in score_ranking_list[:3]]
        summary = " ".join(top_sentences)

        return summary