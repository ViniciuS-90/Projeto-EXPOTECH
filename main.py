from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, value
from graficos import gerar_graficos

# Dados
T = 4  # Semanas
demanda = [80, 60, 50, 40] 
custo_unitario = 2
custo_pedido = 100
custo_estoque = 1
capacidade_pedido = 100
estoque_maximo = 100

# Variáveis
x = {t: LpVariable(f"x_{t}", lowBound=0, upBound=capacidade_pedido) for t in range(T)}
s = {t: LpVariable(f"s_{t}", lowBound=0, upBound=estoque_maximo) for t in range(T)}
Q = {t: LpVariable(f"Q_{t}", cat=LpBinary) for t in range(T)}

# Modelo
model = LpProblem("Gestao_de_Estoque", LpMinimize)

# Função objetivo
model += lpSum([
    custo_unitario * x[t] + custo_pedido * Q[t] + custo_estoque * s[t]
    for t in range(T)
])

# Restrições
for t in range(T):
    model += x[t] <= capacidade_pedido * Q[t]
    if t == 0:
        model += s[t] == x[t] - demanda[t]
    else:
        model += s[t] == s[t-1] + x[t] - demanda[t]


model.solve()

print("=== RESULTADO DA OTIMIZAÇÃO ===")
print("Custo total:", value(model.objective))
for t in range(T):
    print(f"Semana {t+1}: Pedido = {x[t].varValue}, Estoque = {s[t].varValue}")

print(f"\n=== COMPARAÇÃO DE CENÁRIOS ===")


def calcular_custo(pedidos_cenario):
    custo_compras = sum(pedidos_cenario) * custo_unitario
    custo_pedidos_total = sum([1 for p in pedidos_cenario if p > 0]) * custo_pedido
    
    #total no estoque
    estoque_atual = 0
    estoque_total = 0
    estoques = []
    for t in range(T):
        estoque_atual = estoque_atual + pedidos_cenario[t] - demanda[t]
        estoques.append(estoque_atual)
        estoque_total += estoque_atual
    
    custo_estoque_total = estoque_total * custo_estoque
    custo_total = custo_compras + custo_pedidos_total + custo_estoque_total
    
    return custo_total, estoques

# cenários 
cenarios = [
    ("Sem Otimizar", [80, 60, 50, 40]),
    ("Pedidos maiores", [100, 50, 80, 0]),
    ("Balanceada", [90, 50, 90, 0]),
    ("Otimizada (PuLP)", [x[t].varValue for t in range(T)])
]

# Calcular e mostrar resultados
cenarios_dados = {'nomes': [], 'pedidos': [], 'estoques': [], 'custos': []}

for nome, pedidos_cenario in cenarios:
    custo, estoques_cenario = calcular_custo(pedidos_cenario)
    
    print(f"\n{nome}: {[int(p) for p in pedidos_cenario]} → R$ {custo}")
    
    cenarios_dados['nomes'].append(nome.replace(' ', '\n') if len(nome.split()) > 1 else nome)
    cenarios_dados['pedidos'].append(pedidos_cenario)
    cenarios_dados['estoques'].append(estoques_cenario)
    cenarios_dados['custos'].append(custo)
semanas = list(range(1, T+1))
gerar_graficos(semanas, demanda, cenarios_dados)