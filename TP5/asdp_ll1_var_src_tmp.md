
# ASDP LL(1) para `VAR src = "/tmp"`

## Gramática

## 2. Gramática

``` bnf
<programa> ::= <declaracion>
<declaracion> ::= "VAR" <asignacion>
<asignacion> ::= <identificador> "=" <expresion>
<expresion> ::= <string>

| No Terminal | Producción      |
|-------------|-----------------|
| S           | → VAR AsigVar   |
| AsigVar     | → Ident = Valor |
| Ident       | → id            |
| Valor       | → STRING        |

---

## 3. Conjuntos PRIM (FIRST) y SIG (FOLLOW)

### **PRIM**

-   PRIM(P) = PRIM(DECLARACION) = { VAR }
-   PRIM(DECLARACION) = { VAR }
-   PRIM(ASIGNACION) = { ID }
-   PRIM(EXPRESION) = { STRING }

*No hay producciones con λ.*

------------------------------------------------------------------------

### **SIG**

-   SIG(P) = { \$ }
-   SIG(DECLARACION) = { \$ }
-   SIG(ASIGNACION) = { \$ }
-   SIG(EXPRESION) = { \$ }

------------------------------------------------------------------------

## 4. Conjuntos PRED

Como ninguna producción deriva λ, **PRED = PRIM(derecha)**.

-   P → DECLARACION\
    **PRED = { VAR }**

-   DECLARACION → VAR ASIGNACION\
    **PRED = { VAR }**

-   ASIGNACION → ID EQUALS EXPRESION\
    **PRED = { ID }**

-   EXPRESION → STRING\
    **PRED = { STRING }**

## PRIM, SIG, PRED

| Símbolo | PRIM       | SIG   | PRED       |
|---------|------------|-------|------------|
| S       | { VAR }    | { $ } | { VAR }    |
| AsigVar | { id }     | { $ } | { id }     |
| Ident   | { id }     | { = } | { id }     |
| Valor   | { STRING } | { $ } | { STRING } |

---

La gramática es **LL(1)** porque no hay intersecciones entre PRED de un mismo no terminal.

## Tabla LL(1)

| VN \ VT     | VAR             | id                      | = | STRING         | $ |
|-------------|-----------------|-------------------------|---|----------------|---|
| **S**       | S → VAR AsigVar |                         |   |                |   |
| **AsigVar** |                 | AsigVar → Ident = Valor |   |                |   |
| **Ident**   |                 | Ident → id              |   |                |   |
| **Valor**   |                 |                         |   | Valor → STRING |   |

---

## ASDP LL(1) — Movimientos (Tabla A)

| Pila            | Entrada           | Transición              |
|-----------------|-------------------|-------------------------|
| $ S             | VAR id = STRING $ | S → VAR AsigVar         |
| $ AsigVar VAR   | VAR id = STRING $ | Emparejar(VAR)          |
| $ AsigVar       | id = STRING $     | AsigVar → Ident = Valor |
| $ Valor = Ident | id = STRING $     | Ident → id              |
| $ Valor = id    | id = STRING $     | Emparejar(id)           |
| $ Valor =       | = STRING $        | Emparejar('=')          |
| $ Valor         | STRING $          | Valor → STRING          |
| $ STRING        | STRING $          | Emparejar(STRING)       |
| $               | $                 | Aceptar                 |


"La gramática es LL(1) porque para cada no terminal, los conjuntos PRED de sus producciones son disjuntos y la tabla LL(1) no tiene conflictos.