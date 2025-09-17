import ply.lex as lex

# -----------------------
# Palabras clave
# -----------------------
reserved = {
    'SERVIDOR': 'SERVIDOR',
    'GRUPO': 'GRUPO',
    'DESPLEGAR': 'DESPLEGAR',
    'ARCHIVO': 'ARCHIVO',
    'PAQUETE': 'PAQUETE',
    'SERVICIO': 'SERVICIO',
    'EJECUTAR': 'EJECUTAR',
    'COPIAR_DESDE': 'COPIAR_DESDE',
    'EN': 'EN',
    'CON': 'CON',
    'VERIFICAR': 'VERIFICAR',
    'SI': 'SI',
    'NO_EXISTE': 'NO_EXISTE',
    # Para iteración:
    'MIENTRAS': 'MIENTRAS',   # similar a WHILE
    'HACER': 'HACER'
}

# -----------------------
# Tokens
# -----------------------
tokens = [
    'ID',
    'STRING',
    'NUMBER',

    # Operadores
    'EQUALS', 'EQ', 'NEQ', 'GT', 'LT',

    # Símbolos
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
    'LPAREN', 'RPAREN',
    'COLON', 'DASH',
] + list(reserved.values())

# -----------------------
# Expresiones regulares
# -----------------------

# Operadores
t_EQUALS = r'='
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_LT = r'<'

# Símbolos
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_COLON    = r':'
t_DASH     = r'-'

# String: "algo"
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # quitar comillas
    return t

# Números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'ID')  
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Contar líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Errores
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# -----------------------
# Construcción del lexer
# -----------------------
lexer = lex.lex()

# -----------------------
# Prueba
# -----------------------
data = '''
GRUPO webservers {
    SERVIDOR "web01" DIRECCION = "192.168.1.10"
    SERVIDOR "web02" DIRECCION = "192.168.1.11"
}

DESPLEGAR mi_aplicacion EN webservers {
    PAQUETE "nginx" DEBE_ESTAR_INSTALADO
    SERVICIO "nginx" DEBE_ESTAR_EN_EJECUCION
    COPIAR_DESDE "./app/*" HACIA "/var/www/html/"
}

MIENTRAS (VERIFICAR puerto != 80) HACER {
    EJECUTAR "reiniciar nginx"
}
'''

lexer.input(data)
for tok in lexer:
    print(tok)


for tok in lexer:
    print(tok)
