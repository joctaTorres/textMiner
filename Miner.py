import Tokenizer
import TokenWritter


words = Tokenizer('portuguese').tokenizeFileWords('./example.txt')
print(words)