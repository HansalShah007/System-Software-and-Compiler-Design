# -*- coding: utf-8 -*-

"""
Created on Sat Aug 21 14:59:20 2021
@author: Hansal Shah

Write a lex program to count the number of tokens in the given statements.
"""

import ply.lex as lex

tokens = (
"KEYWORD",
"VARNAME",
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
t_SEPARATOR = r';|,'
t_PRTSTR = r'".*"'
t_ignore = ' '

def t_KEYWORD(t):
    r'int|return'
    return t

def t_VARNAME(t):
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

t_OPERATOR = r'\+=|-=|\*=|/=|\+\+|--|==|\+|-|\*|/|='

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
     
def t_error(t):
    print("Illegal character %s"%t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

statements = ['printf("The sum is %d",ans);',
              '22+23*100+x',
              '198x2 = 23.43 + 67;']

for statement in statements:
    print('\nLexical analysis of: '+statement)
    total_tokens = 0
    lexer.input(statement)
    while True:
        tok = lexer.token()
        if not tok: break
        total_tokens+=1
        print(tok)
    
    print('Total tokens =',total_tokens)
    


