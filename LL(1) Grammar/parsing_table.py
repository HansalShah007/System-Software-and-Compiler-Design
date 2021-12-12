# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:37:42 2021

@author: Hansal Shah
@rollno: 19BCP043
@branch: Computer Engineering
@division: 1

Experiment 6:
    Write a program to construct LL(1) parsing table for LL(1) grammar and 
    validate the input string.
"""

grammar = open(r'D:\System Software & Compiler Design\Lab Assignments\Lab 6\grammar.txt', 
               'r',
               encoding='utf-8')
non_terminal_rules = grammar.readlines()

for i in range(len(non_terminal_rules)):
    non_terminal_rules[i] = non_terminal_rules[i][:-1]
    
rules_of_grammar = {}
terminals = []
ll1_table_dict = dict()
not_ll1 = False

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
    
for each in rules_of_grammar:
    for prod in rules_of_grammar[each]:
        for character in prod:
            if not (ord(character)>=65 and ord(character)<=90):
                if character!='\u03B5':
                    terminals.append(character)
                    

terminals = list(set(terminals))
terminals.sort()                 
terminals.append('$')

# Function to find the first of a non-terminal symbol
def get_first(symbol, rules_of_grammar):
    if(symbol in firsts):
        return
    else:
        firsts[symbol] = []
        ll1_table_dict[symbol] = dict()
    nodes = rules_of_grammar[symbol]
    
    for each in nodes:
        for i in range(len(each)):
            stop = False
            
            if ord(each[i])>=65 and ord(each[i])<=90:
                temp =[]
                if(each[i] in firsts):
                    temp = firsts[each[i]]
                    for first in temp:
                        if(first not  in firsts[symbol]):
                            firsts[symbol].append(first)
                            if first in ll1_table_dict[symbol]:
                                print(symbol, first, each)
                                not_ll1 = True
                            else:    
                                if first!='\u03B5':
                                    ll1_table_dict[symbol][first] = each
                else:
                    get_first(each[i], rules_of_grammar)
                    temp = firsts[each[i]]
                    for first in temp:
                        if(first not in firsts[symbol]):
                            firsts[symbol].append(first)
                            if first in ll1_table_dict[symbol]:
                                print(symbol, first, each)
                                not_ll1 = True
                            else:    
                                if first!='\u03B5':
                                    ll1_table_dict[symbol][first] = each
                
                if('\u03B5' not in temp):
                    stop = True
            else:
                if(each[i] not in firsts[symbol]):
                    firsts[symbol].append(each[i])
                    if each[i] in ll1_table_dict[symbol]:
                        print(symbol, each[i], each)
                        not_ll1 = True
                    else:    
                        if each[i]!='\u03B5':
                            ll1_table_dict[symbol][each[i]] = each
                            
                stop = True

            if(stop):
                break
            
#Function to find the follow of a non-terminal symbol                
def get_follow(symbol, rules_of_grammar):
    if(symbol in follows):
        return 
    
    follows[symbol] = []
    for nt in rules_of_grammar:
        for node in rules_of_grammar[nt]:
            if(symbol in node):
                index = node.index(symbol)+1
                
                while(index<len(node)):
                    stop = False
                    
                    if ord(node[index])>=65 and ord(node[index])<=90:
                         temp = firsts[node[index]]
                         for e in temp:
                            if(e!='\u03B5'):
                                if(e not in follows[symbol]):
                                    follows[symbol].append(e)
                         if('\u03B5' not in temp):
                            stop = True
                    else:
                        if(node[index] not in follows[symbol]):
                            follows[symbol].append(node[index])
                        stop = True   
            
                    if(stop): 
                        break
                    
                    index = index+1
                
                if(index==len(node)):
                    temp = []
                    if(nt in follows):
                        temp = follows[nt]
                        for e in temp:
                            if(e not in follows[symbol]):
                                follows[symbol].append(e)
                    else:
                        get_follow(nt, rules_of_grammar)
                        temp = follows[nt]
                        for e in temp:
                            if(e not in follows[symbol]):
                                follows[symbol].append(e)

non_terminal_symbols = list(rules_of_grammar.keys())

# Finding the first of each symbol
firsts ={}    
for each in rules_of_grammar:
    get_first(each, rules_of_grammar)

#Finding the follow of wach symbol
follows = {}
for i in range(len(non_terminal_symbols)):
    get_follow(non_terminal_symbols[i], rules_of_grammar)
    if(i==0):
        follows[non_terminal_symbols[i]].append('$')
        
for symbol in firsts:
    if '\u03B5' in firsts[symbol]:
        for terminal in follows[symbol]:
            if terminal in ll1_table_dict[symbol]:
                print(symbol, terminal, '\u03B5')
                not_ll1 = True
            else:
                ll1_table_dict[symbol][terminal] = '\u03B5'


print('\nGrammar')
for each in non_terminal_symbols:
    print(each+' -> ', end='')
    for i in range(len(rules_of_grammar[each])):
        if i==len(rules_of_grammar[each])-1:
            print(rules_of_grammar[each][i],end='\n')
        else:
            print(rules_of_grammar[each][i]+' | ',end='')
                
if not_ll1:
    print("\nIt is not a LL1 grammar!")
    
else:
    
    print('\nFirst of each non-terminal symbol')
    for each in firsts:
        print(each+':', firsts[each])
            
    print('\nFollow of each non-terminal symbol')
    for each in follows:
        print(each+':', follows[each])
        
    # Printing the LL1 parsing table
    longest_prod = 0
    for symbol in rules_of_grammar:
        for prod in rules_of_grammar[symbol]:
            if len(prod)>longest_prod:
                longest_prod=len(prod)
    
    print('\nThe LL1 parsing table:')
    print('\n  ',end='')
    for each in terminals:
        print(each,' '*(longest_prod-1), end='')
    
    for symbol in non_terminal_symbols:
        print('\n')
        print(symbol,end=' ')
        for terminal in terminals:
            if terminal in ll1_table_dict[symbol]:
                print(ll1_table_dict[symbol][terminal],end='')
                print(' '*(longest_prod-len(ll1_table_dict[symbol][terminal])),end=' ')
            else:
                print('-'+' '*(longest_prod),end='')
                
    string = input("\nEnter the string to be validated: ");
    stack = [non_terminal_symbols[0]]
    index = 0
    valid = True 
    
    while len(stack)!=0:
        try:
            if stack[-1]==string[index]:
                stack.pop()
                index+=1
            else:
                if stack[-1] in non_terminal_symbols:
                    if string[index] in ll1_table_dict[stack[-1]]:
                        prod = ll1_table_dict[stack[-1]][string[index]]
                        stack.pop()
                        for i in range(len(prod)-1, -1, -1):
                            stack.append(prod[i])
                    else:
                        valid = False
                else:
                    valid = False
                    
            if not valid:
                break
            
        except:
            valid = False
            break
        
    if valid:
        print ('String "{}" is a valid string for the given LL1 grammar!'.format(string))
    else:
        print ('String "{}" is not a valid string for the given LL1 grammar!'.format(string))
        