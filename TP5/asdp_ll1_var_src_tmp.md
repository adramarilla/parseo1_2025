
# ASDP LL(1) para `VAR src = "/tmp"`

## Gramática

| No Terminal | Producción |
|-------------|------------|
| S | → VAR AsigVar |
| AsigVar | → Ident = Valor |
| Ident | → id |
| Valor | → STRING |

---

## PRIM, SIG, PRED

| Símbolo | PRIM | SIG | PRED |
|---------|-------|------|-------|
| S | { VAR } | { $ } | { VAR } |
| AsigVar | { id } | { $ } | { id } |
| Ident | { id } | { = } | { id } |
| Valor | { STRING } | { $ } | { STRING } |

---

## Tabla LL(1)

| VN \ VT | VAR | id | = | STRING | $ |
|----------|-----|----|---|---------|---|
| **S** | S → VAR AsigVar |  |  |  |  |
| **AsigVar** |  | AsigVar → Ident = Valor |  |  |  |
| **Ident** |  | Ident → id |  |  |  |
| **Valor** |  |  |  | Valor → STRING |  |

---

## ASDP LL(1) — Movimientos (Tabla A)

| Pila | Entrada | Transición |
|------|----------|------------|
| $ S | VAR id = STRING $ | S → VAR AsigVar |
| $ AsigVar VAR | VAR id = STRING $ | Emparejar(VAR) |
| $ AsigVar | id = STRING $ | AsigVar → Ident = Valor |
| $ Valor = Ident | id = STRING $ | Ident → id |
| $ Valor = id | id = STRING $ | Emparejar(id) |
| $ Valor = | = STRING $ | Emparejar('=') |
| $ Valor | STRING $ | Valor → STRING |
| $ STRING | STRING $ | Emparejar(STRING) |
| $ | $ | Aceptar |

