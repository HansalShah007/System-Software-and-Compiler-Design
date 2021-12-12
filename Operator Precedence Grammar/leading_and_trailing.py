# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 23:08:22 2021

@author: Hansal Shah
@rollno: 19BCP043
@branch: Computer Engineering
@division: 1

Experiment 7:
    Write a program to find leading and trailing of a given grammar where 
    input is taken from the file.
"""


grammar = open(r'D:\System Software & Compiler Design\Lab Assignments\Lab 7\grammar.txt', 
               'r',
               encoding='utf-8')
non_terminal_rules = grammar.readlines()

for i in range(len(non_terminal_rules)):
    non_terminal_rules[i] = non_terminal_rules[i][:-1]
    

#Printing the grammar
print('\nGrammar')
for each in non_terminal_rules:
    print(each)
    
rules_of_grammar = {}

for each in non_terminal_rules:
    raw_production = each
    temp_production = ''
    for i in range(len(raw_production)):
        if(raw_production[i]!=' '):
            temp_production+=raw_production[i]
            
    lhs, rhs = temp_production.split('->')[0], temp_production.split('->')[1] 
    if '|' in rhs:
        rules_of_grammar[lhs] = rhs.split('|')
    else:
        rules_of_grammar[lhs] = [rhs]
    

#Checking whether the grammar is operator precedence or not

operator_precedence = True

for non_terminal in rules_of_grammar:
    for production in rules_of_grammar[non_terminal]:
        
        if '\u03B5' in production:
            operator_precedence = False
            break
        
        variable = None
        if production[0].isalpha():
            varaible = True 
        else:
            variable = False
    
        for i in range(1, len(production)):
            if production[i].isalpha() and variable==True:
                operator_precedence = False
                break
            elif production[i].isalpha() and variable==False:
                variable = True
            elif (not production[i].isalpha()) and variable==False:
                operator_precedence = False
                break
            else:
                variable = False
        
        if not operator_precedence:
            break
        
    if not operator_precedence:
        break
    
    
# Function to find the leading of a non-terminal symbol
def get_leading(symbol, rules_of_grammar):
    if(symbol in leadings):
        return
    else:
        leadings[symbol] = []
    nodes = rules_of_grammar[symbol]
    
    for each in nodes:
        i=0
        if each[i].isalpha() and each[i].isupper():
            if i!=len(each)-1:
                if each[i+1] not in leadings[symbol]:
                    leadings[symbol].append(each[i+1])
            
            if each[i] in leadings:
                for leading in leadings[each[i]]:
                    if leading not in leadings[symbol]:
                        leadings[symbol].append(leading)
            else:
                get_leading(each[i], rules_of_grammar)
                
                for leading in leadings[each[i]]:
                    if leading not in leadings[symbol]:
                        leadings[symbol].append(leading)
        
        else:
            if each[i] not in leadings[symbol]:
                leadings[symbol].append(each[i])
        
                
                
# Function to find the leading of a non-terminal symbol
def get_trailing(symbol, rules_of_grammar):
    if(symbol in trailings):
        return
    else:
        trailings[symbol] = []
    nodes = rules_of_grammar[symbol]
    
    for each in nodes:
        i=len(each)-1
        if each[i].isalpha() and each[i].isupper():
            if i!=0:
                if each[i-1] not in trailings[symbol]:
                    trailings[symbol].append(each[i-1])
            
            if each[i] in trailings:
                for trailing in trailings[each[i]]:
                    if trailing not in trailings[symbol]:
                        trailings[symbol].append(trailing)
            else:
                get_trailing(each[i], rules_of_grammar)
                
                for trailing in trailings[each[i]]:
                    if trailing not in trailings[symbol]:
                        trailings[symbol].append(trailing)
        
        else:
            if each[i] not in trailings[symbol]:
                trailings[symbol].append(each[i])            

                
if operator_precedence:
    print("\nThe grammar is an operator precedence grammar")
    
    non_terminal_symbols = list(rules_of_grammar.keys())

    #Finding the leading of each symbol
    leadings = {}    
    for each in rules_of_grammar:
        get_leading(each, rules_of_grammar)
    
    #Finding the trailing of each symbol
    trailings = {}
    for each in rules_of_grammar:
        get_trailing(each, rules_of_grammar)
               
    print('\nLeading of each non-terminal symbol')
    for each in leadings:
        print(each+':', leadings[each])
        
    print('\nTrailing of each non-terminal symbol')
    for each in trailings:
        print(each+':', trailings[each])
        
else:
    print("\nThe grammar is not an operator precedence grammar, hence leading and trailing cannot be find out")
                    


    
