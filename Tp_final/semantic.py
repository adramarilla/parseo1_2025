class SymbolTable:
    def __init__(self):
        self.variables = {}
        self.groups = {}
        self.servers = {}

    # --- Variables ---
    def add_variable(self, name, value):
        self.variables[name] = value
        print(f"[VAR] {name} = {value}")

    def resolve_value(self, token):
        if token in self.variables:
            return self.variables[token]
        return token

    # --- Grupos y servidores ---
    def add_group(self, name, servers):
        self.groups[name] = [s["nombre"] for s in servers]
        print(f"[GRUPO] {name} con {len(servers)} servidores")

    def add_server(self, name, direccion):
        self.servers[name] = direccion
        print(f"  [SERVIDOR] {name} @ {direccion}")

    def check_group_exists(self, name):
        if name not in self.groups:
            print(f"[Error Semántico] Grupo '{name}' no definido.")
