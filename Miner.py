from Tokenizer import Tokenizer
from TokenWritter import TokenWritter

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

    def search(self):
        pass

    def generateMidFile(self):
        self.writter.outputTokens(
            self.tokenizer.tokenizeFileWords(self.filePath),
            'minerMid.csv'
        )

Miner('./example.txt', ['tag'], ['word']).generateMidFile()