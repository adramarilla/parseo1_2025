from parser import parse_code, symtab
from executor import ejecutar

data = """
GRUPO webservers {
    SERVIDOR "web01" DIRECCION = "192.168.1.10"
    SERVIDOR "web02" DIRECCION = "192.168.1.11"
}

MIENTRAS (VERIFICAR puerto != 80) HACER {
    EJECUTAR "reiniciar nginx"
}

SI (VERIFICAR NO_EXISTE archivo) HACER {
    EJECUTAR "crear archivo de configuración"
}

VAR src = "/tmp"
VAR dest = "/bkp"

DESPLEGAR app EN webservers {
    COPIAR_DESDE src HACIA dest
    PAQUETE "nginx" DEBE_ESTAR_INSTALADO
    SERVICIO "nginx" DEBE_ESTAR_EN_EJECUCION
    EJECUTAR "reiniciar nginx"
}
"""

ast = parse_code(data)
ejecutar(ast, symtab)
