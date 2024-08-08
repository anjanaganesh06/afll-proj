import ply.lex as lex
import ply.yacc as yacc

# List of token names. This is always required
tokens = [
    'NUM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IF',
    'ELSE',
    'INT',
    'ID',
    'STRING',
    'PUTS',
    'END',
    'ASSIGN',
    'WHILE', 
    'GTHAN','LTHAN','EQ','UNTIL'
]

# Define reserved words as a dictionary
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'puts': 'PUTS',
    'end': 'END',
    'while': 'WHILE',
    'until': 'UNTIL'
}

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GTHAN= r'\>'
t_LTHAN= r'\<'
#t_EQ= r'\='
#t_TAB=r'\   '
t_ASSIGN = r'='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_start(p):
    '''start : declaration'''
    print('Valid declaration')

def p_declaration(p):
    
    '''declaration : statements  UNTIL  ops  statements END
    '''

def p_statements(p):
    '''statements : ID ASSIGN NUM
                  | ID ASSIGN ID
    '''

def p_ops(p):
    ''' ops : ID GTHAN NUM
            | ID LTHAN NUM
            | ID GTHAN ASSIGN NUM
            | ID LTHAN ASSIGN NUM
            | ID ASSIGN ASSIGN NUM
            | ID ASSIGN ASSIGN ID
    '''

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

# Test it out
while True:
    try:
        s = input("Enter: ")
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)
