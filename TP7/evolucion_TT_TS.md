
# TT y TS 
## Fragmento analizado

```
L1: VAR archivo = "/etc/config.conf"
L2: 
L3: SI (VERIFICAR NO_EXISTE archivo) HACER {
L4:     EJECUTAR ARCHIVO archivo
L5: }
```

---

# TT (Tabla de Tipos)

## **Estado inicial (antes de procesar L1)**
```
TT vacía → sólo se cargarán tipos primitivos cuando aparezcan en el programa.
```

---

## **Luego de L1: VAR archivo = "/etc/config.conf"**
Se detecta un literal string → se incorpora el tipo `string`.

### TT
| Linea PRG | Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito | Observaciones |
|-----------|-----|--------|----------|-------|-----------|--------|--------|--------|----------------|
| L1        | 0   | string | -1       | -1    | 1         | -1     | -1     | 0      | primitivo      |

---

## **Luego de L3: SI (VERIFICAR NO_EXISTE archivo) ...**
La condición `VERIFICAR NO_EXISTE archivo` devuelve un booleano.  
→ Se agrega el tipo `boolean`.

### TT
| Linea PRG | Cod | Nombre  | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito | Observaciones |
|-----------|-----|---------|----------|-------|-----------|--------|--------|--------|---------------|
| L1        | 0   | string  | -1       | -1    | 1         | -1     | -1     | 0      | primitivo     |
| L3        | 1   | boolean | -1       | -1    | 1         | -1     | -1     | 0      | primitivo     |

---

## **Luego de L4 y L5**
No se introducen nuevos tipos → TT queda igual.

---

# TS (Tabla de Símbolos)

---

## **Estado inicial (antes de L1)**
```
TS vacía
```

---

## **Luego de L1: VAR archivo = "/etc/config.conf"**

### TS
| Linea PRG | Cod | Nombre  | Categoria | Tipo | NumPar | ListaPar | Ámbito | Observaciones |
|-----------|-----|---------|-----------|------|--------|----------|--------|---------------|
| L1        | 0   | archivo | variable  | 0    | -1     | -1       | 0      | inicializada  |

---

## **Luego de L3: uso de archivo en la condición**

`archivo` ya existe → se usa, no se agrega entrada nueva.  
→ Se anotan observaciones.

### TS
| Linea PRG | Cod | Nombre  | Categoria | Tipo | NumPar | ListaPar | Ámbito | Observaciones                                |
|-----------|-----|---------|-----------|------|--------|----------|--------|----------------------------------------------|
| L1        | 0   | archivo | variable  | 0    | -1     | -1       | 0      | inicializada; usada en condición (L3)        |

---

## **Luego de L4: EJECUTAR ARCHIVO archivo**

`archivo` vuelve a usarse → se actualiza observación.

### TS Final
| Linea PRG | Cod | Nombre  | Categoria | Tipo | NumPar | ListaPar | Ámbito | Observaciones                                                |
|-----------|-----|----------|-----------|------|--------|----------|--------|----------------------------------------------------------------|
| L1        | 0   | archivo | variable  | 0    | -1     | -1       | 0      | inicializada (L1); usada en condición (L3) y bloque (L4)      |
