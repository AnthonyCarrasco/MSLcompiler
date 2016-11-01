from scanner import *

def program(tokens):


    if series(tokens):
        if tokens == ["."]:
            return True
        else:
            return series(tokens)

def series(tokens):
    print("entering series routine")
    boolean = statement(tokens)
    print(tokens)
    return True

def statement(tokens):
    print("entering statement routine")
    print(tokens)
    nextChar = tokens.pop()
    print(nextChar)
    if nextChar == "WHILE":
        return while_statement(tokens)
    elif nextChar == "IF":
        return if_statement(tokens)
    elif nextChar == "READ":
        return read_statement(tokens)
    elif nextChar == "WRITE":
        return write_statement(tokens)
    elif nextChar.isalpha():
        tokens.append(nextChar)
        return assign_statement(tokens)
    else:
        return False

def while_statement(tokens):
    print("entering while_statement routine")
    if expression(tokens):
        nextChar = tokens.pop()
        if nextChar == "DO":
            if(series(tokens)):
                nextChar == tokens.pop()
                if nextChar == "OD":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def if_statement(tokens):
    print("entering if_statement routine")
    if expression(tokens):
        nextChar = tokens.pop()
        if nextChar == "THEN":
            if series(tokens):
                if tokens[-1] == "ELSE":
                    tokens.pop()
                    if series(tokens):
                        nextChar == tokens.pop()
                        return nextChar == "FI"
                elif tokens:
                    nextChar = tokens.pop()
                    return nextChar == "FI"
            else:
                return False
        else:
            return False
    else:
        return False

def assign_statement(tokens):
    print("entering assign_statement routine")
    if variable(tokens):
        nextChar = tokens.pop()
        if nextChar == ":=":
            return expression(tokens)
        else:
            return False
    else:
        return False

def read_statement(tokens):
    print("entering read_statement routine")
    if tokens[-1] == "#":
        tokens.pop()
    if variable(tokens):
        if tokens[-1] == ",":
            tokens.pop()
            return read_statement(tokens)
        else:
            return True
    else:
        return False
def write_statement(tokens):
    print("entering wrtie_statement routine")
    if tokens[-1] == "#":
        tokens.pop()
    if expression(tokens):
        if tokens[-1] == ",":
            tokens.pop()
            return write_statement(tokens)
        else:
            return True
    else:
        return False

def variable(tokens):
    print("entering varaible routine")
    nextChar = tokens.pop()
    if nextChar.isalpha():
        if tokens[-1] == "!":
            tokens.pop()
            return operand(tokens)
        else:
            return True
    else:
        return False


def expression(tokens):
    print("entering expression routine")
    if operand(tokens):
        if operator(tokens):
            return operand(tokens)
        elif tokens:
            return True
        else:
            return False
    else:
        return False

def operand(tokens):
    print("entering operand routine")
    nextChar = tokens.pop()
    if nextChar.isdigit() or nextChar.isalpha():
        return True
    elif nextChar == "(":
        if expression(tokens):
            nextChar == tokens.pop()
            if nextChar == ")":
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def operator(tokens):
    print("entering operator routine")
    nextChar = tokens.pop()
    operators = ["<",">","=","<=","==",">=","+","-","/","*","%","&"]
    if nextChar in operators:
        return True
    else:
        return False


lexemes = main()
lexemes.reverse()
print(lexemes)
#boolean = series(lexemes)
boolean = program(lexemes)
print boolean
