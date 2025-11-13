
# ASAB con Retroceso — Ejemplo Completo
# ASAB con Retroceso — Cadena `VAR src = "/tmp"`

Gramática utilizada:

```
S        → VAR AsigVar
AsigVar  → Ident = Valor
Ident    → id
Valor    → STRING
```

Terminales: `VAR`, `id`, `=`, `STRING`, `$`  
Pila inicial: `#`  
Entrada: `VAR id = STRING $`

---

## Tabla de Movimientos (ASAB con retroceso)

| Pila                       | Entrada            | Acción                          |
|----------------------------|--------------------|---------------------------------|
| `#`                        | `VAR id = STRING $`| δ(q0, λ, λ) ⇒ (q1, #S)         |
| `# S`                      | `VAR id = STRING $`| shift                           |
| `# S VAR`                  | `id = STRING $`    | reduce (S → VAR AsigVar)        |
| `# AsigVar`                | `id = STRING $`    | shift                           |
| `# AsigVar id`             | `= STRING $`       | reduce (Ident → id)             |
| `# AsigVar Ident`          | `= STRING $`       | shift                           |
| `# AsigVar Ident =`        | `STRING $`         | shift                           |
| `# AsigVar Ident = STRING` | `$`                | reduce (Valor → STRING)         |
| `# AsigVar Ident = Valor`  | `$`                | reduce (AsigVar → Ident = Valor)|
| `# S`                      | `$`                | accept                          |

---

## Cadena
Se especifica otra palabra distinta.

```
SI ( VERIFICAR NO_EXISTE archivo ) HACER {
    EJECUTAR ARCHIVO archivo
}
```

Tokenizada como:
```
SI ( VERIFICAR NO_EXISTE ID ) HACER { EJECUTAR ARCHIVO ID } $
```

---

# Gramática utilizada
```
S        → IfStmt
IfStmt   → SI LPAREN Cond RPAREN HACER Block
Cond     → VERIFICAR NO_EXISTE ID
Block    → LBRACE Stmt RBRACE
Stmt     → EJECUTAR ARCHIVO ID
```

---

# ASAB con Retroceso (Formato TP6)

| Pila | Entrada | Acción |
|------|---------|--------|
| `#` | `SI ( VERIFICAR NO_EXISTE ID ) HACER { EJECUTAR ARCHIVO ID } $` | δ(q0, λ, λ) ⇒ (#, S) |
| `# S` | `SI ( ...` | expandir S ⇒ IfStmt |
| `# IfStmt` | `SI ( ...` | expandir IfStmt ⇒ SI LPAREN Cond RPAREN HACER Block |
| `# SI LPAREN Cond RPAREN HACER Block` | `SI ( ...` | shift |
| `# SI LPAREN Cond RPAREN HACER Block SI` | `( VERIFICAR ...` | shift |
| `# LPAREN SI Cond RPAREN HACER Block` | `VERIFICAR NO_EXISTE ...` | shift |
| `# VERIFICAR LPAREN SI Cond RPAREN HACER Block` | `NO_EXISTE ID ...` | shift |
| `# NO_EXISTE VERIFICAR LPAREN SI Cond RPAREN HACER Block` | `ID ) ...` | shift |
| `# ID NO_EXISTE VERIFICAR LPAREN SI Cond RPAREN HACER Block` | `) HACER ...` | reduce (Cond → VERIFICAR NO_EXISTE ID) |
| `# Cond LPAREN SI RPAREN HACER Block` | `) HACER ...` | shift |
| `# RPAREN Cond LPAREN SI HACER Block` | `HACER { ...` | shift |
| `# HACER RPAREN Cond LPAREN SI Block` | `{ EJECUTAR ...` | shift |
| `# LBRACE HACER RPAREN Cond LPAREN SI Stmt RBRACE` | `EJECUTAR ARCHIVO ID } ...` | shift |
| `# EJECUTAR LBRACE ... ARCHIVO ID RBRACE` | `ARCHIVO ID } ...` | shift |
| `# ARCHIVO EJECUTAR ... ID RBRACE` | `ID } ...` | shift |
| `# ID ARCHIVO EJECUTAR ... RBRACE` | `} $` | reduce (Stmt → EJECUTAR ARCHIVO ID) |
| `# Stmt LBRACE ... RBRACE` | `} $` | shift |
| `# RBRACE Stmt LBRACE ...` | `$` | reduce (Block → LBRACE Stmt RBRACE) |
| `# Block RPAREN Cond LPAREN SI` | `$` | reduce (IfStmt → SI LPAREN Cond RPAREN HACER Block) |
| `# IfStmt` | `$` | reduce (S → IfStmt) |
| `# S` | `$` | **aceptar** |

---

La cadena completa es **aceptada** por el ASAB con retroceso.
