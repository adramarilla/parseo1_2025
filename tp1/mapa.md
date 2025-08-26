# Mapa conceptual - Compiladores y Traductores

```mermaid
flowchart TD
    np("Traductor") --> n7("Interprete") & n11["Compilador"] & n12["Ensamblador"]
    A["Compiladores y Traductores<br>"] --> np & n10["Herramientas"]
    n12 --> n13["Lenguaje ensamblador →Código máquina"]
    n13 --> n14(["Ventajas"]) & n15(["Desventajas"])
    n15 --> n16["Dependientes de la maquina - Dificiles de escribir/leer<br>"]
    n14 --> n17["Rapidos - Exactos<br>"]
    n11 --> n18["Fuente alto nivel → Objeto bajo nivel"] & n19["Ejecución rápida"] & n20["Analiza todo el programa"]
    n7 --> n21["Traduce y ejecutasentencia por sentencia"]
    n21 --> n22(["Ejemplos: Python, Ruby,JS"])
    n10 --> n23["Editores -&gt; Leer/escribir código fuente<br>Preprocesadores -&gt; Macros, Librerias, Comentarios<br>Enlazadores -&gt; Unen módulos en ejecutable<br>Cargadores -&gt; Asignan memoria, Reubican código<br>Depuradores -&gt; Detectar y corregir errores<br>Desensambladores -&gt; Máquina → Ensamblador<br>Decompiladores -&gt; Máquina → Lenguaje alto nivel<br>Transpilador -&gt; Fuente → Otro lenguaje/versión"]
    n11@{ shape: rounded}
    n12@{ shape: rounded}
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

