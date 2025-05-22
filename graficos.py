import matplotlib.pyplot as plt

def gerar_graficos(semanas, demanda, pedidos, estoques, custos_unitarios, custos_pedidos, custos_estoques):
   
    plt.figure(figsize=(15, 10))
    #Tem que ler da esquerda pra direita
    # 1º Gráfico Pedidos vs Demanda
    plt.subplot(2, 2, 1)
    bars1 = plt.bar([s-0.2 for s in semanas], demanda, width=0.4, label='Demanda', color='#FF6B6B', alpha=0.8)
    bars2 = plt.bar([s+0.2 for s in semanas], pedidos, width=0.4, label='Pedidos', color='#4ECDC4', alpha=0.8)

    plt.xlabel('Semanas')
    plt.ylabel('Quantidade (unidades)')
    plt.title('Estratégia Otimizada: Pedidos vs Demanda', fontweight='bold', fontsize=12)
    plt.legend()
    plt.xticks(semanas)
    plt.grid(True, alpha=0.3)

    # 2º Gráfico Ocupação do Estoque
    plt.subplot(2, 2, 2)
    plt.plot(semanas, estoques, marker='o', linewidth=3, color='#2ECC40', markersize=8)
    plt.fill_between(semanas, estoques, alpha=0.3, color='#2ECC40')
    plt.xlabel('Semanas')
    plt.ylabel('Estoque (unidades)')
    plt.title('Evolução Estratégica do Estoque', fontweight='bold', fontsize=12)
    plt.xticks(semanas)
    plt.grid(True, alpha=0.3)

    # 3º Gráfico Custos Gerais
    plt.subplot(2, 2, 3)
    categorias = ['Compra\nProdutos', 'Custos de\nPedidos', 'Custos de\nEstoque']
    valores = [sum(custos_unitarios), sum(custos_pedidos), sum(custos_estoques)]
    cores = ['#FF9999', '#66B3FF', '#99FF99']

    bars = plt.bar(categorias, valores, color=cores, alpha=0.8)
    for bar, valor in zip(bars, valores):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                 f'R$ {int(valor)}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    plt.ylabel('Custo (R$)')
    plt.title(f'Breakdown de Custos\nTotal: R$ {int(sum(valores))}', fontweight='bold', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')

    # 4º Gráfico Implementação da Otimização
    plt.subplot(2, 2, 4)
    cenarios = ['Sem\nOtimização*', 'Com\nOtimização']
    custos_cenarios = [1000, int(sum(valores))]  
    cores_cenarios = ['#FF6B6B', '#4ECDC4']
    bars = plt.bar(cenarios, custos_cenarios, color=cores_cenarios, alpha=0.8)
    for bar, valor in zip(bars, custos_cenarios):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 10,
                 f'R$ {valor}', ha='center', va='bottom', fontweight='bold', fontsize=12)               
    plt.ylabel('Custo Total (R$)')
    plt.title('Impacto da Otimização', fontweight='bold', fontsize=12)
    plt.text(0.5, 50, '*Estimativa baseada em gestão não otimizada', 
             ha='center', fontsize=8, style='italic', alpha=0.7)
    plt.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.show()