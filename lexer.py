""" The Python Program scans a text file for a set of tokens """
"""       Anthony Carrasco  CS355 Programming Languages      """

''' lex scans for token in a given string '''
def lexer(arg):
    string = arg.split(' ') ##splits the string into tokens by whitespace
    for token in string:
        lookupToken(token) ##call lookupToken to validate


''' lookupToken compares the token to the acceptable token '''
def lookupToken(token):
    ''' Check if each token is a reserved word, integer, or indentifier '''
    if token == "if":
        print(token)
    elif token == "then":
        print(token)
    elif token == "else":
        print(token)
    elif isInt(token): ##calls isInt to check if token is int
        print(token)
    elif token.isalpha():
        print(token)
    else:
        ''' If token is not a reserved word check if it is an operator '''
        exp = token[:] ##splits token into individual character
        for token in exp: #loop through list
            if token == '+':
                print(token)
            elif token == '*':
                print(token)
            elif token == '-':
                print(token)
            elif token == '(':
                print(token)
            elif token == ')':
                print(token)
            elif token == '=':
                print(token)
            elif token == '>':
                print(token)
            elif token == '<':
                print(token)
            elif token == '!':
                print(token)
            elif isInt(token):
                print(token)
            elif token.isalpha():
                print(token)
            else:
                print("_?_")

''' isInt allows lexer to check if a token is a integer '''
''' while avoiding a potential exception being thrown   '''
def isInt(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False

''' main method '''
if __name__ == '__main__':

    file = 'lexer.txt'

    try:
        with open(file) as f_obj:
            fileContents = f_obj
            for lines in fileContents:
                lexer(lines)
    except:
        print('Sorry file not found')
