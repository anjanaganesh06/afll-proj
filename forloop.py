import ply.lex as lex
import ply.yacc as yacc
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
    'DO',
    'DOT',
    'LOOP',
    'PUTS',
    'TO_A',
    'BREAK',
    'IN',
    'GTHAN',
    'LTHAN',
    'FOR'
]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'puts': 'PUTS',
    'end': 'END',
    'to_a': 'TO_A',
    'do'  :'DO',
    'break':'BREAK',
    'loop':'LOOP',
    'puts':'PUTS',
    'in':'IN',
    'for':'FOR'

}

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOLLAR= r'\$'
t_ASSIGN = r'\='
t_DOT= r'\.'
t_GTHAN= r'\>'
t_LTHAN= r'\<'


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

t_ignore = ' \t'



# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_start(p):
    'start : forloop_declaration'

    print('Valid declaration')

def p_dowhile_declaration(p):
    '''forloop_declaration : ID ASSIGN STRING FOR ID IN NUM DOT DOT NUM DO PUTS ID END
                            | FOR ID IN NUM DOT DOT NUM DO ID ASSIGN NUM END
                            '''
    print('DoWhile declaration')


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
