# Projeto-EXPOTECH
# 📊 Gestão de Estoques com Modelagem Matemática

> **Projeto desenvolvido para a EXPOTECH 2025 - UniFECAF**  
> Otimização de pedidos para minimizar custos de armazenagem usando Python e PuLP

## 🎯 **Objetivo**

Desenvolver um sistema automatizado de gestão de estoques que utiliza **modelagem matemática** e **programação linear inteira** para otimizar decisões de pedidos, minimizando custos totais de uma empresa varejista.

## 🔍 **Problema Abordado**

Uma empresa varejista precisa otimizar seu processo de pedidos considerando:
- **Custo de pedido**: R$ 100 por pedido realizado
- **Custo unitário**: R$ 2 por produto comprado  
- **Custo de estoque**: R$ 1 por unidade armazenada
- **Demanda semanal**: [80, 60, 50, 40] unidades
- **Período de análise**: 4 semanas

## 🧮 **Modelagem Matemática**

### Variáveis de Decisão
- `x[t]`: Quantidade pedida na semana t
- `s[t]`: Estoque no final da semana t  
- `Q[t]`: Variável binária (1 = pedido feito, 0 = não)

### Função Objetivo
```
Minimizar: Σ (custo_unitário × x[t] + custo_pedido × Q[t] + custo_estoque × s[t])
```

### Restrições
- Balanço de estoque: `s[t] = s[t-1] + x[t] - demanda[t]`
- Vínculo binário: `x[t] ≤ capacidade_máxima × Q[t]`
- Limites de capacidade e estoque

## 🚀 **Tecnologias Utilizadas**

- **Python 3.x**
- **PuLP**: Programação Linear Inteira
- **Matplotlib**: Visualização de dados
- **NumPy**: Operações matemáticas (nas análises complementares)

## ⚡ **Como Executar**

### 1. **Pré-requisitos**
```bash
pip install pulp matplotlib
```

### 2. **Executar o Projeto**
```bash
python main.py
```

### 3. **Resultados**
O programa irá:
- Resolver o modelo de otimização
- Exibir resultados no terminal
- Gerar gráficos comparativos

## 🎓 **Conceitos Aplicados**

### Operations Research
- Programação Linear Inteira Mista
- Modelagem de problemas reais
- Otimização multiobjetivo

### Matemática Aplicada  
- Álgebra Linear (vetores e matrizes)
- Matemática Discreta (variáveis binárias)
- Análise de cenários

### Programação
- Algoritmos de otimização
- Visualização de dados
- Estruturas de dados

## 📜 **Licença**

Este projeto foi desenvolvido para fins acadêmicos na EXPOTECH 2025 da UniFECAF.

<div align="center">

![UniFECAF](https://img.shields.io/badge/UniFECAF-EXPOTECH%202025-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![PuLP](https://img.shields.io/badge/PuLP-Optimization-green?style=for-the-badge)

</div>
