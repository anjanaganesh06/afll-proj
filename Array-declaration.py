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
    'DOLLAR',
    'DOT',
    'NEW',
    'ARRAY'
]

# Define reserved words as a dictionary
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'puts': 'PUTS',
    'end': 'END',
    'new': 'NEW',
    'Array': 'ARRAY'
}

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOLLAR = r'\$'
t_ASSIGN = r'='
t_DOT = r'\.'

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
    'start : statements'

def p_statements(p):
    '''statements : ID ASSIGN NUM
                  | ID ASSIGN ID
                  | DOLLAR ID ASSIGN NUM
                  | array_declaration
    '''
    print('Valid declaration')

def p_array_declaration(p):
    '''array_declaration : ID ASSIGN ARRAY DOT NEW optional_parameters '''
    print('Array declaration')

def p_optional_parameters(p):
    '''optional_parameters : LPAREN NUM RPAREN
                          | LPAREN  RPAREN
    '''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error")

# def t_dot(t):
#     r'\.'
#     return t

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
