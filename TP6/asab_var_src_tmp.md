
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

## Observaciones
- La gramática no presenta ambigüedad, por lo que no se requieren retrocesos explícitos.

