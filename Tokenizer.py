from nltk.tokenize import word_tokenize as wt
from nltk.tokenize import PunktSentenceTokenizer as pt
from nltk import pos_tag as pt

import string


class Tokenizer():
    lang = ''

    def __init__(self, lang):
        self.lang = lang

    def tokenizeFileWords(self, path):
        return self.tokenize(
            self.openFile(path)
        )

    def openFile(self, path):
        return open(path, "r").read()

    def tokenize(self, text):
        tokenizer = pt(text)
        tSentences =  tokenizer.tokenize(text)
        punkt = []
        for sentence in tSentences:
            try:
                words = wt(sentence)
                punkt.append(pt(words)) 
            except Exception as e:
                print('Could not tokenize sentence, reason:', str(e))
        return punkt

    def preprocess(self, text):
        punctuations = r'''!()-[]{};:'"’\,<>./?@#$%^&*_~'''
        no_punct = ""
        for char in text:
            if char not in punctuations:
               no_punct = no_punct + char
        return no_punct


words = Tokenizer('portuguese').tokenizeFileWords('./example.txt')
print(words)
