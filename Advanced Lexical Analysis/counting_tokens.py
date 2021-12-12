# -*- coding: utf-8 -*-

"""
Created on Sat Aug 21 14:59:20 2021
@author: Hansal Shah

Write a LEX program to eliminate comment lines in a C/python program and 
copy the resulting program into a separate file, Write LEX program to 
recognize valid identifier, operators and keywords in the given text file. 
Count the number of tokens in the given grammar.
"""

import ply.lex as lex

tokens = (
"DIRECTIVE",
"COMMENTS",
"KEYWORD",
"BLOCKRPAREN",
"BLOCKLPAREN",
"IDENTIFIER",
"INVNAME",
"INT",
"FLOAT",
"LPAREN",
"RPAREN",
"OPERATOR",
"SEPARATOR",
"PRTSTR"
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BLOCKLPAREN = r'\{'
t_BLOCKRPAREN = r'\}'
t_SEPARATOR = r';|,'
t_OPERATOR = r'\+=|-=|\*=|/=|\+\+|--|==|\+|-|\*|/|='
t_PRTSTR = r'".*"'
t_ignore = ' '

def t_DIRECTIVE(t):
    r'\#.*'
    pass

def t_COMMENTS(t):
    r'//.*'
    pass

def t_KEYWORD(t):
    r'int|return'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    return t

def t_INVNAME(t):
    r'[0-9]+[a-zA-Z]+[0-9]*';
    print('Invalid character %s'%t.value)
    t.lexer.skip(1)
    
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
     
def t_error(t):
    print("Illegal character %s"%t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

addition_file = open(r'D:\System Software & Compiler Design\Lab Assignments\Lab 2\addition.txt', 'r')
lines = addition_file.readlines()
data = ''

for line in lines:
    data = data + line

total_tokens = 0
print('\nLexical analysis for program in addition.txt')
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok: break
    total_tokens+=1
    print(tok)

print('Total tokens =',total_tokens)

