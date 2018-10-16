from Miner import Miner

class Minecart():
    miner = None

    def menu(self):
        print('1- Load file')
        self.push()
        print('2- Search in file')
        self.beat()


    def push(self):
        file = input('Enter file name or path: ')
        print('Opening: ./' + file + '.txt ...')
        self.miner = Miner('./' + file + '.txt')
    
    def beat(self):
        listwords = []
        listtags = []

        try:
            typedwords = input('Enter list of words: ')
            listwords = typedwords.split()
        except SyntaxError:
            listwords = []
        
        try:
            typedtags = input('Enter list of tags: ')
            listtags = typedtags.split()        
        except SyntaxError:
            listtags = []

        
        if(listtags == [] and listwords == []):
            print('You\'ve typed an empty query')
            return

        if(listtags == []):
            df = self.miner.search(
                tags=[],
                words=listwords
                )
            print(df)
            return

        if(listwords == []):
            df = self.miner.search(
                tags=listtags,
                words=[]
                )
            print(df)
            return
        
        df = self.miner.search(tags=listtags, words=listwords)
        print(df)
        return

Minecart().menu()