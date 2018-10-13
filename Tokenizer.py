from nltk.tokenize import word_tokenize as wt
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
        return wt(self.preprocess(text))

    def preprocess(self, text):
        punctuations = r'''!()-[]{};:'"’\,<>./?@#$%^&*_~'''
        no_punct = ""
        for char in text:
            if char not in punctuations:
               no_punct = no_punct + char
        return no_punct


words = Tokenizer('english').tokenizeFileWords('./example.txt')
print(words)
