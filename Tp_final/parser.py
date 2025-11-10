import ply.yacc as yacc
from lexer import tokens

# -----------------------
# Reglas de la gramática
# -----------------------

def p_programa(p):
    '''programa : definiciones instrucciones'''
    print("Programa válido")

def p_definiciones(p):
    '''definiciones : definiciones definicion
                    | empty'''

def p_definicion(p):
    '''definicion : GRUPO ID LBRACE servidores RBRACE'''

def p_servidores(p):
    '''servidores : servidores servidor
                  | servidor'''

def p_servidor(p):
    '''servidor : SERVIDOR STRING DIRECCION EQUALS STRING'''

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion
                     | empty'''

def p_instruccion(p):
    '''instruccion : despliegue
                   | condicional
                   | bucle
                   | asignacion'''

def p_despliegue(p):
    '''despliegue : DESPLEGAR ID EN ID LBRACE acciones RBRACE'''

def p_acciones(p):
    '''acciones : acciones accion
                | accion'''

def p_accion(p):
    '''accion : PAQUETE STRING DEBE_ESTAR_INSTALADO
              | SERVICIO STRING DEBE_ESTAR_EN_EJECUCION
              | COPIAR_DESDE STRING HACIA STRING
              | EJECUTAR STRING'''

def p_condicional(p):
    '''condicional : SI LPAREN VERIFICAR condicion RPAREN HACER LBRACE acciones RBRACE
                   | SI LPAREN VERIFICAR condicion RPAREN HACER LBRACE acciones RBRACE SINO LBRACE acciones RBRACE'''

def p_bucle(p):
    '''bucle : MIENTRAS LPAREN VERIFICAR condicion RPAREN HACER LBRACE acciones RBRACE'''

def p_asignacion(p):
    '''asignacion : VAR ID EQUALS valor'''

def p_valor(p):
    '''valor : STRING
             | NUMBER'''

def p_condicion(p):
    '''condicion : ID comparador valor'''

def p_comparador(p):
    '''comparador : EQ
                  | NEQ
                  | GT
                  | LT'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

# -----------------------
# Parser
# -----------------------
parser = yacc.yacc()

# -----------------------
# Prueba
# -----------------------
data = '''
GRUPO webservers {
    SERVIDOR "web01" DIRECCION = "192.168.1.10"
}

DESPLEGAR app EN webservers {
    PAQUETE "nginx" DEBE_ESTAR_INSTALADO
    SERVICIO "nginx" DEBE_ESTAR_EN_EJECUCION
    COPIAR_DESDE "./app/*" HACIA "/var/www/html/"
}
'''

parser.parse(data)

