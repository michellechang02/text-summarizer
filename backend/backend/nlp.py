import re
import nltk
import math
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

class TextSummarizer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.ps = PorterStemmer()

    def create_frequency_table(self, text) -> dict:
        words = word_tokenize(text)
        freq_table = {}
        for word in words:
            curr = self.ps.stem(word)
            if curr not in self.stop_words:
                if curr in freq_table:
                    freq_table[curr] += 1
                else:
                    freq_table[curr] = 1
        return freq_table

    def score_sentences(self, sentences, freq_table) -> dict:
        sentence_value = {}
        for sentence in sentences:
            word_count_in_sentence = len(word_tokenize(sentence))
            for word_value in freq_table:
                if word_value in sentence.lower():
                    sentence_key = sentence[:10]
                    if sentence_key in sentence_value:
                        sentence_value[sentence_key] += freq_table[word_value]
                    else:
                        sentence_value[sentence_key] = freq_table[word_value]

            sentence_value[sentence[:10]] //= word_count_in_sentence

        return sentence_value

    def find_average_score(self, sentence_value) -> int:
        sum_values = sum(sentence_value.values())
        return int(sum_values / len(sentence_value))

    def summarize_text(self, sentences, sentence_value, threshold):
        summary = ''
        for sentence in sentences:
            if sentence[:10] in sentence_value and sentence_value[sentence[:10]] > threshold:
                summary += " " + sentence
        return summary

    def generate_summary(self, text_input) -> str:
        freq_table = self.create_frequency_table(text_input)
        print(freq_table)
        sentences = sent_tokenize(text_input)
        print(sentences)
        sentence_scores = self.score_sentences(sentences, freq_table)
        print(sentence_scores)
        threshold = self.find_average_score(sentence_scores)
        print(threshold)
        summary = self.summarize_text(sentences, sentence_scores, threshold * 1.5)
        print(summary)
        return summary
