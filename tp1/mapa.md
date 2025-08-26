# Mapa conceptual - Compiladores y Traductores

```mermaid
mindmap
   root((Compiladores y Traductores))
    Traductor
        "Convierte de lenguaje fuente a lenguaje objeto"
            Ejemplo: "C → Pascal"
        Ensamblador
            "Lenguaje ensamblador → Código máquina"
                Ventajas
                    "Rápidos"
                    "Exactos"
                Desventajas
                    "Difíciles de escribir/leer"
                    "Dependientes de la máquina"
        Intérprete
            "Traduce y ejecuta sentencia por sentencia"
                Ejemplos: "Python, Ruby, JS"
        Compilador
            "Fuente alto nivel → Objeto bajo nivel"
            "Analiza todo el programa"
            "Ejecución rápida"
    Herramientas
      Editores
        "Leer/escribir código fuente"
        "Integrados en IDE"
      Preprocesadores
        "Sustituir macros"
        "Incluir librerías"
        "Eliminar comentarios"
      Enlazadores
        "Unen módulos en ejecutable"
        "Vinculan librerías"
      Cargadores
        "Asignan memoria"
        "Reubican código"
      Depuradores
        "Detectar y corregir errores"
      Desensambladores
        "Máquina → Ensamblador"
      Decompiladores
        "Máquina → Lenguaje alto nivel"
      Transpilador
        "Fuente → Otro lenguaje/versión"
