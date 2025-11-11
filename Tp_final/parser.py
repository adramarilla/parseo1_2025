import ply.yacc as yacc
from lexer import tokens
from semantic import SymbolTable

symtab = SymbolTable()
ast = []

# -----------------------
# GRAMÁTICA PRINCIPAL
# -----------------------

def p_programa(p):
    '''programa : definiciones instrucciones'''
    p[0] = ("programa", p[1], p[2])
    global ast
    ast = p[0]

# -----------------------
# DEFINICIONES DE GRUPOS
# -----------------------
def p_definiciones(p):
    '''definiciones : definiciones definicion
                    | definicion
                    | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_definicion(p):
    '''definicion : GRUPO ID LBRACE servidores RBRACE'''
    p[0] = ("grupo", p[2], p[4])
    symtab.add_group(p[2], p[4])

def p_servidores(p):
    '''servidores : servidores servidor
                  | servidor'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_servidor(p):
    '''servidor : SERVIDOR STRING DIRECCION EQUALS STRING'''
    p[0] = {"nombre": p[2], "direccion": p[5]}
    symtab.add_server(p[2], p[5])

# -----------------------
# INSTRUCCIONES
# -----------------------
def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion
                     | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_instruccion(p):
    '''instruccion : despliegue
                   | asignacion
                   | bucle
                   | condicional'''
    p[0] = p[1]

# -----------------------
# VARIABLES
# -----------------------
def p_asignacion(p):
    '''asignacion : VAR ID EQUALS valor'''
    symtab.add_variable(p[2], p[4])
    p[0] = ("var", p[2], p[4])

def p_valor(p):
    '''valor : STRING
             | NUMBER'''
    p[0] = p[1]

# -----------------------
# DESPLIEGUE
# -----------------------
def p_despliegue(p):
    '''despliegue : DESPLEGAR ID EN ID LBRACE acciones RBRACE'''
    p[0] = ("desplegar", p[2], p[4], p[6])
    symtab.check_group_exists(p[4])

def p_acciones(p):
    '''acciones : acciones accion
                | accion'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_accion(p):
    '''accion : PAQUETE STRING DEBE_ESTAR_INSTALADO
              | SERVICIO STRING DEBE_ESTAR_EN_EJECUCION
              | COPIAR_DESDE origen HACIA destino
              | EJECUTAR STRING'''
    if p[1] == "COPIAR_DESDE":
        p[0] = ("copiar", p[2], p[4])
    elif p[1] == "PAQUETE":
        p[0] = ("paquete", p[2])
    elif p[1] == "SERVICIO":
        p[0] = ("servicio", p[2])
    elif p[1] == "EJECUTAR":
        p[0] = ("ejecutar", p[2])

def p_origen(p):
    '''origen : STRING
              | ID'''
    p[0] = symtab.resolve_value(p[1])

def p_destino(p):
    '''destino : STRING
               | ID'''
    p[0] = symtab.resolve_value(p[1])

# -----------------------
# CONDICIONAL
# -----------------------
def p_condicional(p):
    '''condicional : SI LPAREN VERIFICAR condicion RPAREN HACER LBRACE acciones RBRACE
                   | SI LPAREN VERIFICAR condicion RPAREN HACER LBRACE acciones RBRACE SINO LBRACE acciones RBRACE'''
    if len(p) == 10:
        p[0] = ("si", p[4], p[8])
    else:
        p[0] = ("si_sino", p[4], p[8], p[12])

# -----------------------
# BUCLE
# -----------------------
def p_bucle(p):
    '''bucle : MIENTRAS LPAREN VERIFICAR condicion RPAREN HACER LBRACE acciones RBRACE'''
    p[0] = ("mientras", p[4], p[8])

# -----------------------
# CONDICIONES
# -----------------------
def p_condicion(p):
    '''condicion : ID NEQ valor
                 | ID EQ valor
                 | ID GT valor
                 | ID LT valor
                 | NO_EXISTE ID'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = ("no_existe", p[2])

# -----------------------
# VACÍO / ERROR
# -----------------------
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: fin inesperado")

parser = yacc.yacc()

def parse_code(data):
    parser.parse(data)
    return ast
