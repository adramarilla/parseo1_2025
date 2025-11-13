# TP Introducción

## Lenguaje a crear

**Lenguaje de Configuración y Despliegue para Servicios (Estilo Ansible simplificado)**

---

## Objetivo

Realizar una herramienta de automatización para configuración de servidores y ejecutar acciones de manera declarativa.
En este TP se define el componente léxico del lenguaje. El lexer toma un archivo de texto y lo convierte en una secuencia de tokens, que luego serán usados por el parser
---

## Especificaciones léxicas

- **Palabras clave:**  
Estas palabras tienen un significado fijo en el lenguaje y no pueden ser usadas como nombres.
 `VAR`,`SERVIDOR`, `GRUPO`, `DESPLEGAR`, `ARCHIVO`, `PAQUETE`, `SERVICIO`,  
  `EJECUTAR`, `COPIAR_DESDE`, `HACIA`, `EN`, `CON`, `VERIFICAR`, `NO_EXISTE`,
  `DIRECCION`, `HACER`, `DEBE_ESTAR_INSTALADO`, `DEBE_ESTAR_EN_EJECUCION`, 
  `SI`,`SINO`,`MIENTRAS`

- **Identificadores:**  
  Nombres de servidores (`"web01"`, `"db_production"`),  
  nombres de grupos (`"webservers"`, `"databases"`),  
  nombres de paquetes (`"nginx"`, `"nodejs"`),  
  rutas (`"/var/www/app"`).

- **Literales:**  
  STRING (para comandos, rutas, contenido), NUMBER (para puertos), ID (para nombre de servidores, grupos, ruta sin comillas)

- **Operadores:**  
  `=`, `==`, `!=`, `>`, `<` (para comparaciones en verificaciones).

- **Símbolos:**  
  `{`, `}`, `[`, `]`, `(`, `)`, `:`, `-` (para bloques, listas y parámetros).

---

## Reglas léxicas
Cada token se define mediante una expresión regular. Por ejemplo:

• Un ID es una secuencia de letras, números y guiones bajos que empieza con letra.
• Un STRING es cualquier texto entre comillas dobles.
• Los números se reconocen como secuencias de dígitos.
• Las palabras reservadas se detectan antes y se cargan en el diccionario reserved.

## Especificaciones sintácticas

### Ejemplo de definición de grupo de servidores

```plaintext
GRUPO webservers {
    SERVIDOR "web01" DIRECCION = "192.168.1.10"
    SERVIDOR "web02" DIRECCION = "192.168.1.11"
}
```
---
### Ejemplo de tarea de despliegue

```plaintext
DESPLEGAR mi_aplicacion EN webservers {

    # Garantizar que un paquete está instalado
    PAQUETE "nginx" DEBE_ESTAR_INSTALADO

    # Garantizar que un servicio está ejecutándose
    SERVICIO "nginx" DEBE_ESTAR_EN_EJECUCION

    # Copiar archivos locales al servidor
    COPIAR_DESDE "./app/*" HACIA "/var/www/html/"
}
```

---

## Especificaciones semánticas

- Verificar que los grupos y servidores referenciados en un `DESPLEGAR ... EN` existan.  
- **Análisis de tipos:** Asegurar que `DIRECCION` sea un *string* y que el puerto en `VERIFICAR` sea un número.  
- **Chequeos de contexto:** No permitir `COPIAR_DESDE` fuera de un bloque `DESPLEGAR`.  
- **Tabla de símbolos:** Llevar un registro de todos los servidores, grupos y sus propiedades.

---
## Resumen
El lexer convierte el texto fuente en una secuencia de tokens que el parser podrá procesar sin ambigüedades.