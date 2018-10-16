from Tokenizer import Tokenizer
from TokenWritter import TokenWritter
import pandas as pd
import pickle

class Miner():
    filePath = ''
    tokenizer = Tokenizer('portuguese')
    writter = TokenWritter()

    def __init__(self, path):
        if (path == ''):
            raise ValueError('Path for file cannot be empty.')
        self.filePath = path
        self.load()

    def load(self):
        self.writeDataframe(
            self.generateDataframe()
        )
        
    def search(self, tags=[], words=[]):
        if (tags == [] and words == []):
            raise ValueError('You must search for a tag or a word, or both.')
            
        df = next(self.readDataframe())
        
        if (tags == []):
            return df[df['PALAVRA'].isin(words)]
        
        if (words == []):
            return df[df['TAG'].isin(tags)]

        wdf = df[df['PALAVRA'].isin(words)]
        return wdf[wdf['TAG'].isin(tags)]
        
        
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
