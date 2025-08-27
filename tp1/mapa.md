# Mapa conceptual - Compiladores y Traductores

```mermaid
flowchart TD
    A["Compiladores y Traductores<br>"] --> np("Traductor") & n10["Herramientas"]
    np --> n7("Intérprete") & n11["Compilador"] & n12["Ensamblador"]

    %% Ensamblador
    n12 --> n13["Lenguaje ensamblador → Código máquina"]
    n13 --> n14(["Ventajas"]) & n15(["Desventajas"])
    n14 --> n17["Rápidos - Exactos"]
    n15 --> n16["Dependientes de la máquina<br>Difíciles de escribir/leer"]

    %% Intérprete
    n7 --> n21["Traduce y ejecuta<br>sentencia por sentencia"]
    n21 --> n22(["Ejemplos: Python, Ruby, JS, BASIC"])

    %% Compilador
    n11 --> n18["Fuente alto nivel → Objeto bajo nivel"] & n19["Ejecución rápida"] & n20["Analiza todo el programa"]
    n11 --> n24["Genera ejecutable binario"]
    n11 --> n25(["Ejemplo histórico: Grace Hopper (A-0, 1951) desarrolla el primer compilador"])

    %% Diferencias
    A --> n26["Diferencias"]
    n26 --> n27["Intérprete → ejecución inmediata"]
    n26 --> n28["Compilador → programa ejecutable"]

    %% Herramientas
    n10 --> n23["Editores → Leer/escribir código fuente<br>Preprocesadores → Macros, Librerías, Comentarios<br>Enlazadores → Unen módulos en ejecutable<br>Cargadores → Asignan memoria y reubican código<br>Depuradores → Detectar y corregir errores<br>Desensambladores → Máquina → Ensamblador<br>Decompiladores → Máquina → Lenguaje alto nivel<br>Transpilador → Fuente → Otro lenguaje/versión"]

    %% Fases compilación
    n11 --> n29["Fases de compilación"]
    n29 --> n30["Análisis: léxico, sintáctico, semántico"]
    n29 --> n31["Síntesis: código intermedio, optimización, código final"]

    %% Estilos
    n11@{ shape: rounded}
    n12@{ shape: rounded}
    n7@{ shape: rounded}
    A@{ shape: dbl-circ}
    n10@{ shape: rounded}
    n13@{ shape: rounded}
    n16@{ shape: lin-proc}
    n17@{ shape: lin-proc}
    n18@{ shape: rounded}
    n19@{ shape: rounded}
    n20@{ shape: rounded}
    n21@{ shape: rounded}
    n23@{ shape: comment}
    n24@{ shape: rounded}
    n25@{ shape: lin-proc}
    n26@{ shape: rounded}
    n27@{ shape: lin-proc}
    n28@{ shape: lin-proc}
    n29@{ shape: rounded}
    n30@{ shape: lin-proc}
    n31@{ shape: lin-proc}

    style np stroke:#00C853,stroke-width:4px,stroke-dasharray: 0
    style n7 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n11 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n12 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style A fill:#FFE0B2,stroke-width:4px,stroke-dasharray: 0,stroke:#FF6D00,color:#000000
    style n10 stroke:#D50000,stroke-width:4px,stroke-dasharray: 0
    style n13 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n14 stroke-width:4px,stroke-dasharray: 0,stroke:#FF6D00,fill:#FFE0B2
    style n15 stroke-width:4px,stroke-dasharray: 0,stroke:#FF6D00,fill:#FFE0B2
    style n18 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n19 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n20 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n21 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n22 stroke-width:4px,stroke-dasharray: 0,stroke:#FFD600,fill:#FFF9C4
    style n23 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n24 stroke-width:4px,stroke-dasharray: 0,fill:#C8E6C9,stroke:#00C853
    style n25 stroke-width:4px,stroke-dasharray: 0,stroke:#2962FF,fill:#E3F2FD
    style n26 stroke-width:4px,stroke-dasharray: 0,stroke:#FF6D00,fill:#FFE0B2
    style n27 stroke-width:4px,stroke-dasharray: 0,stroke:#00BFA5,fill:#B2DFDB
    style n28 stroke-width:4px,stroke-dasharray: 0,stroke:#00BFA5,fill:#B2DFDB
    style n29 stroke-width:4px,stroke-dasharray: 0,stroke:#AA00FF,fill:#F3E5F5
    style n30 stroke-width:4px,stroke-dasharray: 0,stroke:#6A1B9A,fill:#E1BEE7
    style n31 stroke-width:4px,stroke-dasharray: 0,stroke:#6A1B9A,fill:#E1BEE7

