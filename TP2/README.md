# TP Introducción

## Lenguaje a crear

**Lenguaje de Configuración y Despliegue para Servicios (Estilo Ansible simplificado)**

---

## Objetivo

Realizar una herramienta de automatización para configuración de servidores y ejecutar acciones de manera declarativa.

---

## Especificaciones léxicas

- **Palabras clave:**  
  `SERVIDOR`, `GRUPO`, `DESPLEGAR`, `ARCHIVO`, `PAQUETE`, `SERVICIO`,  
  `EJECUTAR`, `COPIAR_DESDE`, `EN`, `CON`, `VERIFICAR`, `SI`, `NO_EXISTE`

- **Identificadores:**  
  Nombres de servidores (`"web01"`, `"db_production"`),  
  nombres de grupos (`"webservers"`, `"databases"`),  
  nombres de paquetes (`"nginx"`, `"nodejs"`),  
  rutas (`"/var/www/app"`).

- **Literales:**  
  Strings (para comandos, rutas, contenido) y números (para puertos).

- **Operadores:**  
  `=`, `==`, `!=`, `>`, `<` (para comparaciones en verificaciones).

- **Símbolos:**  
  `{`, `}`, `[`, `]`, `(`, `)`, `:`, `-` (para bloques, listas y parámetros).

---

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
