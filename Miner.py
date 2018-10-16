from Tokenizer import Tokenizer
from TokenWritter import TokenWritter
import pandas as pd
import pickle

class Miner():
    filePath = ''
    searchTag = []
    searchWord = []
    tokenizer = Tokenizer('portuguese')
    writter = TokenWritter()

    def __init__(self, path, tag, word):
        if (path == ''):
            raise ValueError('Path for file cannot be empty.')
        if (tag is [] and word is []):
            raise ValueError('You must search for a tag or a word, or both.')

        self.filePath = path
        self.searchTag = tag
        self.searchWord = word

        self.load()

    def load(self):
        self.writeDataframe(
            self.generateDataframe()
        )
        
    def search(self):
        pass
        
    def generateDataframe(self):
        self.generateMidFile()
        df = pd.read_csv('./minerMid.csv', sep=',', header=0)
        df['count'] = df.groupby(['PALAVRA', 'TAG'])['PALAVRA'].transform('count')
        df.drop_duplicates(inplace=True)
        df.sort_values(by=['count'], ascending=False , inplace=True, kind='quicksort')
        return df
    
    def writeDataframe(self, df):
        fileDf = open('dataframe.pickle', 'wb')
        pickle.dump(df, fileDf)
        fileDf.close()
    
    def readDataframe(self):
        file = open('dataframe.pickle', 'rb')
        yield pickle.load(file)
        file.close()

    def generateMidFile(self):
        self.writter.outputTokens(
            self.tokenizer.tokenizeFileWords(self.filePath),
            'minerMid.csv'
        )

Miner('./example.txt', ['tag'], ['word']).search()