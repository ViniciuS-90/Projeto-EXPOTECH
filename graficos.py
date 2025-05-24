import matplotlib.pyplot as plt

def gerar_graficos(semanas, demanda, cenarios_dados):
    cores = ['#FF6B6B', '#FFB347', '#87CEEB', '#32CD32']  
    
    
    plt.figure(figsize=(15, 10))

    # Gráfico 1 Pedidos
    plt.subplot(2, 2, 1)
    width = 0.2
    x_pos = range(1, 5)
    
    for i in range(len(cenarios_dados['nomes'])):
        positions = [x + width*i for x in x_pos]
        nome = cenarios_dados['nomes'][i].replace('\n', ' ')
        plt.bar(positions, cenarios_dados['pedidos'][i], width=width, 
                label=nome, alpha=0.8, color=cores[i])

    plt.xlabel('Semanas')
    plt.ylabel('Unidades p/ Pedido')
    plt.title('Volume por Semana', fontweight='bold', fontsize=12)
    plt.legend(fontsize=9)
    plt.xticks([x + width*1.5 for x in x_pos], ['1', '2', '3', '4'])
    plt.grid(True, alpha=0.3)

    # Gráfico 2  Estoque
    plt.subplot(2, 2, 2)
    
    for i in range(len(cenarios_dados['nomes'])):
        nome = cenarios_dados['nomes'][i].replace('\n', ' ')
        plt.plot(semanas, cenarios_dados['estoques'][i], marker='o', linewidth=2, 
                 label=nome, alpha=0.8, color=cores[i])

    plt.xlabel('Semanas')
    plt.ylabel('Estoque (unidades)')
    plt.title('Ocupação do Estoque', fontweight='bold', fontsize=12)
    plt.legend(fontsize=9)
    plt.xticks(semanas)
    plt.grid(True, alpha=0.3)

    # Gráfico 3 Demanda
    plt.subplot(2, 2, 3)
    
    plt.plot(semanas, demanda, marker='s', linewidth=3, markersize=8,
             color='#8B0000', alpha=0.9, label='Demanda')
    for i, valor in enumerate(demanda):
        plt.text(semanas[i], valor + 2, str(valor), ha='center', va='bottom', 
                fontweight='bold', fontsize=10)
    
    plt.xlabel('Semanas')
    plt.ylabel('Demanda (unidades)')
    plt.title('Demanda por Semana', fontweight='bold', fontsize=12)
    plt.legend(fontsize=9)
    plt.xticks(semanas)
    plt.grid(True, alpha=0.3)
    plt.ylim(0, max(demanda) * 1.2)  
    
    # Gráfico 4 Custos
    plt.subplot(2, 2, 4)
    
    bars = plt.bar(cenarios_dados['nomes'], cenarios_dados['custos'], 
                   color=cores[:len(cenarios_dados['nomes'])], alpha=0.8)
    
   
    for bar, custo in zip(bars, cenarios_dados['custos']):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                 f'R$ {int(custo)}', ha='center', va='bottom', fontweight='bold', fontsize=10)

    plt.ylabel('Custo Total (R$)')
    plt.title('Comparação de Custos - Todos os Cenários', fontweight='bold', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()
