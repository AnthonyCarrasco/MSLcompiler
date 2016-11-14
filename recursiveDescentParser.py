''' Recursive Descent Parser '''
''' It verifies the list of tokens from scanner/lexer'''
''' Are valid for MSL Grammar '''

''' Import the lexer '''
from scanner import *

''' The grammar is as follows '''
''' Program -> [RESERVE int] { PROC-DEC } series "." '''
def program(tokens):
    print("entering program routine")
    if not tokens:
        return True
    if tokens[-1] == "RESERVE":
        tokens.pop()
        if tokens[-1].isdigit():
            print("RESERVED MEMORY :: " + tokens.pop())
        else:
            return False

    if tokens[-1] == "PROC":
        if  proc_dec(tokens):
            if series(tokens):
                if tokens == ["."]:
                    return True
        else:
            return False
    print("PROC DEC PASSED")
    if series(tokens):
        if tokens == ["."]:
            print(tokens)
            return True
        else:
            return program(tokens)


''' PROCDEC -> PROC identifier ["(" identifier {"," identifier} ")"] series END '''
def proc_dec(tokens):
    print("entering proc_dec")
    nextChar = tokens.pop() #obtain next token
    if nextChar == "PROC":
        nextChar = tokens.pop()
        if nextChar.isalpha():
            if tokens[-1] == "(":
                tokens.pop()
                nextChar = tokens.pop()
                if nextChar.isalpha():
                    nextChar = tokens.pop()
                    if nextChar == ")":
                        if series(tokens):
                            if tokens[-1] == "END":
                                tokens.pop()
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif nextChar == ",":
                        nextChar = tokens.pop()
                        while(nextChar.isalpha()):
                            nextChar = tokens.pop()
                            print(nextChar)
                            if nextChar == ",":
                                nextChar = tokens.pop()
                            elif nextChar == ")":
                                if series(tokens):
                                    if tokens[-1] == "END":
                                        tokens.pop()
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                nextChar = tokens.pop()

''' series -> statement { 'statement' } '''
def series(tokens):
    print("entering series routine")
    boolean = statement(tokens)
    return True

''' statement -> assign | while | if | call | read | write '''
def statement(tokens):
    print("entering statement routine")
    if tokens[-1] == "." or tokens[-1] == "END":
        return True
    nextChar = tokens.pop()
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

''' while -> WHILE expression DO series OD '''
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


''' if-> IF expression THEN series[ELSE series] FI '''
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

''' assign -> variable ":=" expression '''
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
''' read -> READ [#]varaible { "," [#] variable} '''
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

''' write -> WRITE [#] expression { "," [#] expression } '''
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

''' variable -> identifier ["!" operand] '''
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

''' expression -> operand { operator operand' } '''
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

''' operand -> int | text | variable | "(" expression ")" '''
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

''' operator -> All possible operators '''
def operator(tokens):
    print("entering operator routine")
    nextChar = tokens.pop()
    operators = ["<",">","=","<=","==",">=","+","-","/","*","%","&", "!"]
    if nextChar in operators:
        return True
    else:
        return False


''' Main Program to run '''

lexemes = main() #Call the lexer to return a list of tokens
lexemes.reverse() #reverse tokens to treat as a stack
print(lexemes) # print to verify
boolean = program(lexemes) #program returns true or false
print boolean
