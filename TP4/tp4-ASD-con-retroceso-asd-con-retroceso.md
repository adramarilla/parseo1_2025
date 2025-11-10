# TP 4 — Análisis Sintáctico Descendente con Retroceso  
## Cadena: `VAR src = "/tmp"`

---

### 📘 Gramática

1. P → DECLARACION  
2. DECLARACION → VAR ASIGNACION  
3. ASIGNACION → ID EQUALS EXPRESION  
4. EXPRESION → STRING  

---

### 📗 Tokens (según lexer)

| Token  | Lexema   | Descripción            |
|:-------|:---------|:-----------------------|
| VAR    | `VAR`    | Palabra reservada      |
| ID     | `src`    | Identificador          |
| EQUALS | `=`      | Operador de asignación |
| STRING | `"/tmp"` | Cadena literal         |

---

### 🧩 Derivación paso a paso

|        **Pila**       |    **Cadena**    |       **Transición**                              |
|:----------------------|:-----------------|:--------------------------------------------------|
| λ                     | VAR src = "/tmp" | δ(q0, λ, λ) ⇒ (q1, #)                            |
| #                     | VAR src = "/tmp" | δ(q1, λ, λ) ⇒ (q2, S)                            |
| #S                    | VAR src = "/tmp" | δ(q2, λ, S) ⇒ (q2, DECLARACION)                  |
| # DECLARACION         | VAR src = "/tmp" | δ(q2, λ, DECLARACION) ⇒ (q2, VAR ASIGNACION)     |
| # ASIGNACION VAR      | VAR src = "/tmp" | δ(q2, VAR, VAR) ⇒ (q2, λ)                        |
| # ASIGNACION          | src = "/tmp"     | δ(q2, λ, ASIGNACION) ⇒ (q2, ID EQUALS EXPRESION) |
| # EXPRESION EQUALS ID | src = "/tmp"     | δ(q2, λ, ID) ⇒ (q2, src)                         |
| # EXPRESION EQUALS src| src = "/tmp"     | δ(q2, src, src) ⇒ (q2, λ)                        |
| # EXPRESION EQUALS    | = "/tmp"         | δ(q2, λ, EQUALS) ⇒ (q2, =)                       |
| # EXPRESION =         | = "/tmp"         | δ(q2, =, =) ⇒ (q2, λ)                            |
| # EXPRESION           | "/tmp"           | δ(q2, λ, EXPRESION) ⇒ (q2, STRING)               |
| # STRING              | "/tmp"           | δ(q2, λ, STRING) ⇒ (q2, "/tmp")                  |
| # "/tmp"              | "/tmp"           | δ(q2, "/tmp", "/tmp") ⇒ (q2, λ)                  |
| #                     | λ                | δ(q2, λ, #) ⇒ (q3, λ)                            |
| λ                     | λ                | **accept**                                        |

