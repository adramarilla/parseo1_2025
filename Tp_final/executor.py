def ejecutar(ast, symtab):
    print("\n--- EJECUCIÓN ---")
    for nodo in ast[2]:
        tipo = nodo[0]

        if tipo == "desplegar":
            nombre_app = nodo[1]
            grupo = nodo[2]
            acciones = nodo[3]
            servidores = symtab.groups.get(grupo, [])
            print(f"[Desplegando] {nombre_app} en grupo {grupo}: {servidores}")
            for accion in acciones:
                ejecutar_accion(accion)

        elif tipo == "mientras":
            condicion = nodo[1]
            acciones = nodo[2]
            print(f"[MIENTRAS] {condicion}")
            ejecutar_bucle(condicion, acciones)

        elif tipo in ("si", "si_sino"):
            condicion = nodo[1]
            acciones = nodo[2]
            print(f"[SI] {condicion}")
            ejecutar_condicional(condicion, acciones)


def ejecutar_accion(accion):
    tipo = accion[0]
    if tipo == "copiar":
        print(f"  Copiando de {accion[1]} hacia {accion[2]}")
    elif tipo == "paquete":
        print(f"  Asegurando paquete '{accion[1]}' instalado")
    elif tipo == "servicio":
        print(f"  Asegurando servicio '{accion[1]}' en ejecución")
    elif tipo == "ejecutar":
        print(f"  Ejecutando comando: {accion[1]}")


def ejecutar_bucle(condicion, acciones):
    print(f"    (Evaluar condición: {condicion})")
    for _ in range(2):  # simula 2 iteraciones
        for accion in acciones:
            ejecutar_accion(accion)


def ejecutar_condicional(condicion, acciones):
    print(f"    (Evaluar condición: {condicion})")
    for accion in acciones:
        ejecutar_accion(accion)
