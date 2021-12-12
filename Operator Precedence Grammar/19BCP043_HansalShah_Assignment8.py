# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:04:27 2021

@author: Hansal Shah
@rollno: 19BCP043
@branch: Computer Engineering
@division: 1

Experiment 8:
    Write a program to construct operator precedence parsing table for the 
    given grammar and check the validity of the string (id+id*id).
"""


grammar = open(r'D:\System Software & Compiler Design\Lab Assignments\Lab 8\grammar.txt', 
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
        if production[0].isalpha() and production[0].isupper():
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


# Extracting all the terminal symbols
terminal_symbols = {}
index = 0
starting_symbol = None

for non_terminal in rules_of_grammar:
    if index==0:
        starting_symbol = non_terminal
        
    for production in rules_of_grammar[non_terminal]:
        
        for i in range(len(production)):
            if not (production[i].isalpha() and production[i].isupper()):
                if production[i] not in terminal_symbols:
                    terminal_symbols[production[i]] = index
                    index+=1
                    
terminal_symbols['$'] = index
index+=1

print(terminal_symbols)


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
        
    
    # Building the parsing table
    
    # Initializing the parsing table
    parsing_table = [[] for _ in range(len(terminal_symbols))]
    for each in parsing_table:
        for _ in range(len(terminal_symbols)):
            each.append(' ')

    
    # Filling the parsing table
    for non_terminal in rules_of_grammar:
        for production in rules_of_grammar[non_terminal]:
            
            if len(production)==1:
                continue
            
            for i in range(1,len(production)):
                
                if production[i].isalpha() and production[i].isupper():
                    
                    for terminal in leadings[production[i]]:
                        parsing_table[terminal_symbols[production[i-1]]][terminal_symbols[terminal]] = '<'
                
                else:
                    
                    for terminal in trailings[production[i-1]]:
                        parsing_table[terminal_symbols[terminal]][terminal_symbols[production[i]]] = '>'
    
    
    for terminal in list(terminal_symbols.keys()):
        # Adding an accept character in the parsing table for validating the string
        if terminal == '$':
            parsing_table[terminal_symbols['$']][terminal_symbols['$']] = 'A'
        else:
            parsing_table[terminal_symbols[terminal]][terminal_symbols['$']] = '>'
            parsing_table[terminal_symbols['$']][terminal_symbols[terminal]] = '<'
        
  
    # Since '(' and ')' have same precedence
    if ('(' in list(terminal_symbols.keys())) and '(' in list(terminal_symbols.keys()):
        parsing_table[terminal_symbols['(']][terminal_symbols[')']] = '='
        parsing_table[terminal_symbols[')']][terminal_symbols['(']] = '='
        
    
    
    # Printing the parsing table
    print('\n\nParsing table\n')
    print('  | ',end='')
    print(' '.join(list(terminal_symbols.keys())), end='\n')
    print('--+-',end='')
    print('-'*((len(terminal_symbols)*2)))
    
    
    for i in range(len(parsing_table)):
        print(list(terminal_symbols.keys())[i]+' | ',end='')
        print(' '.join(parsing_table[i]),end='\n')

    # Validating the input string 
    string = input("\nEnter the string to be validated: ");    
    string+='$'
    
    stack = ['$'] #Initializing stack
    top = 0
    pointer = 0

    operator_precedence_grammar = False
    while True:
        
        if pointer < len(string):
            entry = parsing_table[terminal_symbols[stack[top]]][terminal_symbols[string[pointer]]]
            if entry == '<' or entry == '=':
                stack.append(string[pointer])
                top+=1
                pointer+=1
            elif entry == '>':
                stack.pop()
                top-=1
            elif entry == 'A':
                operator_precedence_grammar = True
                break
            else:
                break
            
        else:
            break

    if operator_precedence_grammar:
        print('\nValid string! It belongs to the grammar')
    else:
        print('\nInvalid string! It does not belong to the grammar')
            
else:
    print("\nThe grammar is not an operator precedence grammar, hence leading and trailing cannot be find out")
                    


    