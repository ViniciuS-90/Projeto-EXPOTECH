from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, value
from graficos import gerar_graficos  # Importa a função de gráficos

T = 4  
demanda = [80, 60, 50, 40]  # demanda semanal
custo_unitario = 2
custo_pedido = 100
custo_estoque = 1
capacidade_pedido = 100
estoque_maximo = 100


x = {t: LpVariable(f"x_{t}", lowBound=0, upBound=capacidade_pedido) for t in range(T)}  # quantidade pedida
s = {t: LpVariable(f"s_{t}", lowBound=0, upBound=estoque_maximo) for t in range(T)}     # estoque
Q = {t: LpVariable(f"Q_{t}", cat=LpBinary) for t in range(T)}                           # pedido feito?


model = LpProblem("Gestao_de_Estoque", LpMinimize)

model += lpSum([
    custo_unitario * x[t] + custo_pedido * Q[t] + custo_estoque * s[t]
    for t in range(T)
])

for t in range(T):
    model += x[t] <= capacidade_pedido * Q[t]
    if t == 0:
        model += s[t] == x[t] - demanda[t]
    else:
        model += s[t] == s[t-1] + x[t] - demanda[t]


model.solve()

print("Status:")
print("Custo total:", value(model.objective))
for t in range(T):
    print(f"Semana {t+1}: Pedido = {x[t].varValue}, Estoque = {s[t].varValue}, Pedido feito = {Q[t].varValue}")


semanas = list(range(1, T+1))
pedidos = [x[t].varValue for t in range(T)]
estoques = [s[t].varValue for t in range(T)]
pedidos_feitos = [Q[t].varValue for t in range(T)]

# custos
custos_unitarios = [custo_unitario * x[t].varValue for t in range(T)]
custos_pedidos = [custo_pedido * Q[t].varValue for t in range(T)]
custos_estoques = [custo_estoque * s[t].varValue for t in range(T)]

gerar_graficos(semanas, demanda, pedidos, estoques, custos_unitarios, custos_pedidos, custos_estoques)

print(f"\n=== RESUMO ===")
print(f"Custo total otimizado: R$ {value(model.objective):.2f}")
print(f"Total pedido: {sum(pedidos)} unidades")
print(f"Total demanda: {sum(demanda)} unidades")