from Tokenizer import Tokenizer
from TokenWritter import TokenWritter


tokenizer = Tokenizer('portuguese')

TokenWritter().outputTokens(
    tokenizer.tokenizeFileWords('./example.txt'),
    'outputtest.csv'
    )
