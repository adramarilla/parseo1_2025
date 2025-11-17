from parser import parse_code, symtab
from executor import ejecutar

data = '''
GRUPO webservers {
    SERVIDOR "web01" DIRECCION = "192.168.1.10"
    SERVIDOR "web02" DIRECCION = "192.168.1.11"
}

MIENTRAS (VERIFICAR puerto != 80) HACER {
    EJECUTAR "reiniciar nginx"
}

SI (VERIFICAR NO_EXISTE archivo_conf) HACER {
    EJECUTAR ARCHIVO archivo_conf
}

VAR src = "/tmp"
VAR dest = "/bkp"
VAR archivo_conf = "/etc/config.conf"

'''

ast = parse_code(data)
ejecutar(ast, symtab)
