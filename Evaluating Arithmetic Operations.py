# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:48:34 2021

@author: Hansal Shah
@rollno: 19BCP043
@branch: Computer Engineering
@division: 1

Experiment 4:
    Write a YACC program to evaluate arithmetic expression involving operators: 
    +, -, *, /, and ^ (power).
"""

import ply.yacc as yacc
import ply.lex as lex

tokens = (
"INT",
"FLOAT",
"NAME",
"PLUS",
"MINUS",
"TIMES",
"DIVIDE",
"EXPONENT",
"LPAREN",
"RPAREN",
"EQUALS"
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'\='

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
     
def t_error(t):
    print("Illegal character %s"%t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

def p_calc(p):
    '''
    calc : expression
    | var_assign
    | empty
    '''
    print(p[1])

def p_expression_int_float(p):
    '''
    expression : INT 
    | FLOAT
    '''
    p[0] = p[1]
    
def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] =('var', p[1])
    
def p_expression(p):
    '''
    expression : expression TIMES expression
    | expression DIVIDE expression
    | expression PLUS expression
    | expression MINUS expression
    | expression EXPONENT expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    p[0] = ('=', p[1], p[3])
    
precedence = (('left', 'PLUS', 'MINUS'),
              ('left', 'TIMES', 'DIVIDE'),
              ('right', 'EXPONENT'))

def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None
    
parser=yacc.yacc()

while True:
    try:
        s = input("Enter the expression: ")
    except EOFError:
        break
    parser.parse(s)
    