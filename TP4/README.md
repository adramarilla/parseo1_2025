# ✅ TP 4 — Análisis Sintáctico Descendente con Retroceso (ASD con Backtracking)

## Cadena a analizar:
**VAR src = "/tmp"**

## Gramátic

```
<programa> ::= <declaracion>
<declaracion> ::= "VAR" <asignacion>
<asignacion> ::= <identificador> "=" <expresion>
<expresion> ::= <string>
```

---

## 🎯 Objetivo del TP4
Explicar cómo un analizador descendente con retroceso (ASD-B) recorre la cadena, eligiendo producciones y retrocediendo si alguna opción falla.

En este caso la gramática no es ambigua, pero igual se realiza el procedimiento.
---

## 🟢 Resultado final

✔ La cadena  
`VAR src = "/tmp"`  
es aceptada por el ASD con retroceso.

✔ No fue necesario retroceder en ningún punto, porque la gramática es lineal y determinística.

---

## 🧾 Conclusión del TP4
Se aplicó un analizador descendente con retroceso a la cadena indicada.

Se mostraron todas las configuraciones del parser: pila, entrada y transición.

La cadena fue completamente reconocida y se alcanzó el estado de aceptación.

No hubo conflictos ni necesidad real de retroceso, lo cual era esperable por la simpleza de la gramática.