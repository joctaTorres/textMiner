from nltk.tokenize import word_tokenize as wt
from nltk.tokenize import PunktSentenceTokenizer as pt
from nltk import pos_tag as ptag
from nltk.corpus import mac_morpho
import nltk
import pickle
import string


class Tokenizer():
    lang = ''

    def __init__(self, lang):
        self.lang = lang

    def tokenizeFileWords(self, path):
        return self.tokenize(
            self.preprocess(
                self.openFile(path)
            )
        )

    def openFile(self, path):
        return open(path, "r").read()

    def tokenize(self, text):
        #customTagger = self.train()
        train_file = open("trainedTagger.pickle", "rb")
        customTagger = pickle.load(train_file)
        train_file.close()
        punktTokenizer = pt(text)
        tSentences =  punktTokenizer.tokenize(text)
        punkt = []
        for sentence in tSentences:
            try:
                words = wt(sentence)
                punkt.append(customTagger.tag(words))
            except Exception as e:
                print('Could not tokenize sentence, reason:', str(e))
        return punkt

    '''def train(self):
        tsents = mac_morpho.tagged_sents()
        tsents = [[(w.lower(), self.simplify_tag(t)) for (w,t) in sent] for sent in tsents if sent]
        train = tsents[100:]
        test = tsents[:100]
        tagger0 = nltk.DefaultTagger('n')
        tagger1 = nltk.UnigramTagger(train, backoff=tagger0)
        tagger2 = nltk.BigramTagger(train, backoff=tagger1)        
        return nltk.TrigramTagger(train, backoff=tagger2)

    def simplify_tag(self, t):
        if "+" in t:
            return t[t.index("+")+1:]
        else:
            return t'''

    def preprocess(self, text):
        punctuations = r'''!()-[]{};:'"’\,<>./?@#$%^&*_~'''
        no_punct = ""
        for char in text:
            if char not in punctuations:
               no_punct = no_punct + char
        return no_punct



words = Tokenizer('portuguese').tokenizeFileWords('./example.txt')
print(words)
