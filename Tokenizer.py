from nltk.tokenize import word_tokenize as wt


class Tokenizer():
    def __init__(self):
        pass

    def tokenizeFile(self, path):
        return self.tokenize(
            self.openFile(path)
        )

    def openFile(self, path):
        return open(path, "r").read()

    def tokenize(self, text):
        return wt(text)


words = Tokenizer().tokenizeFile('./example.txt')

print(words)
