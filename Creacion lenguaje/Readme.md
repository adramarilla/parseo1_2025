# Análisis Léxico y Próximos Pasos para el Parser

## Explicación

### Palabras clave
→ Se reconocen por `reserved`.

### Tokens genéricos
- `ID`
- `STRING` 
- `NUMBER`

### Operadores
- `=`
- `==` 
- `!=`
- `<`
- `>`

### Símbolos
- `{ }`
- `[ ]`
- `( )`
- `:`
- `-`

### Ejemplo de iteración
`MIENTRAS ... HACER { ... }` ya agregado en el lexer, aunque todavía no tiene gramática.

## 👉 Próximo paso

Definir un parser (`ply.yacc`) con reglas para:

- `GRUPO`
- `DESPLEGAR`
- `PAQUETE` 
- `SERVICIO`
- etc.

y tu nuevo bloque `MIENTRAS ... HACER { instrucciones }`