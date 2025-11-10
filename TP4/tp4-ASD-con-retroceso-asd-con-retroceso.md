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
| λ                     | VAR src = "/tmp" | δ(q0, λ, λ) ⇒ (q1, Z)                            |
| Z                     | VAR src = "/tmp" | δ(q1, λ, λ) ⇒ (q2, P)                            |
| Z P                   | VAR src = "/tmp" | δ(q2, λ, P) ⇒ (q2, DECLARACION)                  |
| Z DECLARACION         | VAR src = "/tmp" | δ(q2, λ, DECLARACION) ⇒ (q2, VAR ASIGNACION)     |
| Z ASIGNACION VAR      | VAR src = "/tmp" | δ(q2, VAR, VAR) ⇒ (q2, λ)                        |
| Z ASIGNACION          | src = "/tmp"     | δ(q2, λ, ASIGNACION) ⇒ (q2, ID EQUALS EXPRESION) |
| Z EXPRESION EQUALS ID | src = "/tmp"     | δ(q2, λ, ID) ⇒ (q2, src)                         |
| Z EXPRESION EQUALS src| src = "/tmp"     | δ(q2, src, src) ⇒ (q2, λ)                        |
| Z EXPRESION EQUALS    | = "/tmp"         | δ(q2, λ, EQUALS) ⇒ (q2, =)                       |
| Z EXPRESION =         | = "/tmp"         | δ(q2, =, =) ⇒ (q2, λ)                            |
| Z EXPRESION           | "/tmp"           | δ(q2, λ, EXPRESION) ⇒ (q2, STRING)               |
| Z STRING              | "/tmp"           | δ(q2, λ, STRING) ⇒ (q2, "/tmp")                  |
| Z "/tmp"              | "/tmp"           | δ(q2, "/tmp", "/tmp") ⇒ (q2, λ)                  |
| Z                     | λ                | δ(q2, λ, Z) ⇒ (q3, λ)                            |
| λ                     | λ                | **accept**                                        |

