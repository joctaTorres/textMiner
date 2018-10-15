class TokenWritter():
    def outputTokens(self, tokens, path):
        if(path == ''):
            print('File name not valid')
            return
       
        with open(path, 'w') as file:
            file.write('PALAVRA, TAG \n')

            for token in tokens[0]:
                try:
                    word = str(token[0]).lower()
                    tag = str(token[1]).lower()
                    if (tag == ''): continue
                    file.write(word + ', ' + tag + '\n')
                except Exception as e:
                    print('Could not write token to file, reason:', str(e))

            file.close()

