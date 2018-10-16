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
        typedwords = input('Enter list of words: ')
        typedtags = input('Enter list of tags: ')
        listwords = typedwords.split()
        listtags = typedtags.split()
     
        df = self.miner.search(
            tags=listtags,
            words=listwords
            )
        
        print(df)

Minecart().menu()