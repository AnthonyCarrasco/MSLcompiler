""" The Python Program scans a text file for a set of tokens """
"""       Anthony Carrasco  CS299 Programming Languages      """


def main():
    file = 'lexer.txt'

    with open(file) as f_obj:
        fileContents = f_obj
        lexemes = []
        for lines in fileContents:
            lexer(lines,lexemes)
        #print lexemes
    return lexemes


''' lex scans for token in a given string '''
def lexer(lines,lexemes):
    string = lines[:] ##splits the string into tokens by whitespace
    token = ""
    for s in string:
        if not s.isspace():
            if s.isalpha() or s.isdigit():
                token += s
            elif s == "<" or s == ">" or s == ":" or s == "=":
                token += s
            else:
                tokenize(s, lexemes)
        else:
            tokenize(token,lexemes)
            token = ""

''' while avoiding a potential exception being thrown   '''
def tokenize(lexeme,lexemes):
    if lexeme == "":
        return
    if lexeme == "*":
        lexemes.append(lexeme)
    elif lexeme == "+":
        lexemes.append(lexeme)
    elif lexeme == ":=":
        lexemes.append(lexeme)
    elif lexeme == "=":
        lexemes.append(lexeme)
    elif lexeme == ">" or lexeme == "<":
        lexemes.append(lexeme)
    elif lexeme == ">=" or lexeme == "<=":
        lexemes.append(lexeme)
    elif lexeme == "(" or lexeme == ")":
        lexemes.append(lexeme)
    elif lexeme == "IF" or lexeme == "THEN" or lexeme == "ELSE":
        lexemes.append(lexeme)
    elif lexeme == "CALL" or "WRITE" or "READ":
        lexemes.append(lexeme)
    elif lexeme == "DO" or lexeme == "OD":
        lexemes.append(lexeme)
    elif lexeme == "FI":
        lexemes.append(lexeme)
    elif lexeme == ",":
        lexemes.append(lexeme)
    elif lexeme == "#":
        lexemes.append(lexeme)
    elif lexeme == "{" or lexeme == "}":
        lexemes.append(lexeme)
    elif lexeme[0].isdigit() and not lexeme.isalpha():
        lexemes.append(int(lexeme))
    elif lexeme.isalpha() and not lexeme.isdigit():
        lexemes.append(lexeme)
    else:
        lexemes.append("Invalid Token")
