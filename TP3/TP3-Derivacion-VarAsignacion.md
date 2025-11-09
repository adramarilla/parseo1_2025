# TP 3 — Árbol y Derivaciones de la cadena `VAR src = "/tmp"`

## Programa de entrada

```
VAR src = "/tmp"
```
---
## BNF correspondiente

```bnf
<programa> ::= <declaracion>

<declaracion> ::= "VAR" <asignacion>

<asignacion> ::= <identificador> "=" <expresion>

<expresion> ::= <string>
```

---
## Gramática utilizada

### GIC = ⟨V, Σ, S, P⟩

- **V (No terminales)** = { P, DECLARACION, ASIGNACION, EXPRESION }  
- **Σ (Terminales)** = { VAR, ID, EQUALS (=), STRING }  
- **S (Símbolo inicial)** = P  
- **P (Producciones):**
  1. P → DECLARACION  
  2. DECLARACION → VAR ASIGNACION  
  3. ASIGNACION → ID EQUALS EXPRESION  
  4. EXPRESION → STRING  

---

## Árbol de Derivación (Gráfico)

```mermaid
flowchart TD
  A[P] --> A1[DECLARACION]
  A1 --> A2["VAR"]
  A1 --> A3[ASIGNACION]

  A3 --> B1[ID]
  A3 --> B2["="]
  A3 --> B3[EXPRESION]

  B1 --> C1["src"]
  B3 --> C2["STRING"]
  C2 --> C3["/tmp"]
```
![Árboles de derivación ASD y ASA](A_pair_of_parse_trees_depicted_in_a_2D_digital_ill.png)

---

## ASD — Derivación por la izquierda (descendente)

| Cadena de derivación obtenida | Próxima producción a aplicar     |
|-------------------------------|----------------------------------|
| P                             | P → DECLARACION                  |
| DECLARACION                   | DECLARACION → VAR ASIGNACION     |
| VAR ASIGNACION                | ASIGNACION → ID EQUALS EXPRESION |
| VAR ID EQUALS EXPRESION       | EXPRESION → STRING               |
| VAR ID EQUALS STRING          | Sustituir ID → src               |
| VAR src EQUALS STRING         | Sustituir STRING → "/tmp"        |
| VAR src EQUALS "/tmp"         | accept                           |

**Resultado:**  
✅ La cadena `VAR src = "/tmp"` se deriva correctamente **por la izquierda** (análisis descendente).

---

## ASA — Derivación por la derecha (reducción ascendente)

| Cadena de derivación obtenida | Próxima producción a aplicar |
|-------------------------------|------------------------------|
| VAR src = "/tmp" | "/tmp" → EXPRESION |
| VAR src = EXPRESION | ID EQUALS EXPRESION → ASIGNACION |
| VAR ASIGNACION | VAR ASIGNACION → DECLARACION |
| DECLARACION | DECLARACION → P |
| P | accept |

**Resultado:**  
✅ La cadena `VAR src = "/tmp"` es reconocida correctamente **por la derecha** (análisis ascendente).

---


## Conclusión

- La palabra `VAR src = "/tmp"` pertenece al lenguaje.  
- Es generada tanto por la derivación **izquierda (ASD)** como **derecha (ASA)**.  
- La gramática cumple las propiedades necesarias para la representación de una **asignación declarativa** dentro del lenguaje.
