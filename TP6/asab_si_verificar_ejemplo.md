
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
Se especifica otra cadena distinta del lenguaje.

```
SI ( VERIFICAR NO_EXISTE archivo_conf ) HACER {
    EJECUTAR ARCHIVO archivo_conf
}
```

Tokenizada como:
```
SI ( VERIFICAR NO_EXISTE ID ) HACER { EJECUTAR ARCHIVO ID } $
```
---

# BNF utilizada

``` bnf
P → IF_STMT

IF_STMT → SI LPAREN COND RPAREN HACER BLOCK

COND → VERIFICAR NO_EXISTE ID

BLOCK → LBRACE STMT RBRACE

STMT → EJECUTAR ARCHIVO ID
```

No terminales: `P, IF_STMT, COND, BLOCK, STMT`\
Terminales:
`SI, LPAREN, RPAREN, VERIFICAR, NO_EXISTE, ID, HACER, LBRACE, RBRACE, EJECUTAR, ARCHIVO`\
Símbolo inicial: `P`

------------------------------------------------------------------------

## 2. **Tabla de reducciones (ASAB)**

  Secuencia en la pila                  Reducir a
  ------------------------------------- -----------
  `EJECUTAR ARCHIVO ID`                 `STMT`
  `LBRACE STMT RBRACE`                  `BLOCK`
  `VERIFICAR NO_EXISTE ID`              `COND`
  `SI LPAREN COND RPAREN HACER BLOCK`   `IF_STMT`
  `IF_STMT`                             `P`

------------------------------------------------------------------------

## 3. **Entrada tokenizada**

    SI LPAREN VERIFICAR NO_EXISTE ID RPAREN HACER LBRACE EJECUTAR ARCHIVO ID RBRACE $


## 4. **Simulación completa del ASAB**

  ----------------------------------------------------------------------------------
  **Pila**                **Entrada**                             **Transición**
  ----------------------- --------------------------------------- ------------------
  λ                       SI ( VERIFICAR NO_EXISTE ID ) HACER {   δ(q0,λ,λ) → (#)
                          EJECUTAR ARCHIVO ID } \$                

  \#                      SI ... \$                               shift(SI)

  \# SI                   ( VERIFICAR NO_EXISTE ID ) HACER {      shift(LPAREN)
                          EJECUTAR ARCHIVO ID } \$                

  \# SI LPAREN            VERIFICAR NO_EXISTE ID ) ...            shift(VERIFICAR)

  \# SI LPAREN VERIFICAR  NO_EXISTE ID ) ...                      shift(NO_EXISTE)

  \# SI LPAREN VERIFICAR  ID ) ...                                shift(ID)
  NO_EXISTE                                                       

  \# SI LPAREN VERIFICAR  ) HACER ...                             reduce → COND
  NO_EXISTE ID                                                    

  \# SI LPAREN COND       ) HACER ...                             shift(RPAREN)

  \# SI LPAREN COND       HACER { EJECUTAR...                     shift(HACER)
  RPAREN                                                          

  \# SI LPAREN COND       { EJECUTAR ARCHIVO ID } \$              shift(LBRACE)
  RPAREN HACER                                                    

  \# SI LPAREN COND       EJECUTAR ARCHIVO ID } \$                shift(EJECUTAR)
  RPAREN HACER LBRACE                                             

  \# ... EJECUTAR         ARCHIVO ID } \$                         shift(ARCHIVO)

  \# ... EJECUTAR ARCHIVO ID } \$                                 shift(ID)

  \# ... EJECUTAR ARCHIVO } \$                                    reduce → STMT
  ID                                                              

  \# ... LBRACE STMT      } \$                                    shift(RBRACE)

  \# ... LBRACE STMT      \$                                      reduce → BLOCK
  RBRACE                                                          

  \# SI LPAREN COND       \$                                      reduce → IF_STMT
  RPAREN HACER BLOCK                                              

  \# IF_STMT              \$                                      reduce → P

  \# P                    \$                                      **Aceptar**
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

## 5. **Conclusión**

La cadena es aceptada por el analizador sintáctico ascendente con
backtracking (ASAB).

------------------------------------------------------------------------