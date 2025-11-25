import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- Parâmetros ---
NUM_LINHAS = 93000

# --- Listas de Possíveis Valores ---
produtos = ['Sapato Social', 'Tênis Esportivo', 'Camisa Polo', 'Calça Jeans',
            'Sapatilha Casual', 'Tênis Corrida', 'Camiseta Básica', 'Calça Moletom',
            'Bota Couro', 'Chinelo', 'Blusa Manga Longa', 'Shorts Sarja']

lojas = [f'Loja {i:02d}' for i in range(1, 21)] # 10 Lojas (Loja 01 a Loja 20)

# Faixa de valores unitários (preços médios)
preco_min_max = {
    'Sapato': (80.00, 250.00),
    'Tênis': (60.00, 300.00),
    'Camisa': (40.00, 150.00),
    'Calça': (50.00, 180.00),
    'Sapatilha': (30.00, 120.00),
    'Bota': (100.00, 350.00),
    'Chinelo': (10.00, 50.00),
    'Blusa': (35.00, 110.00),
    'Shorts': (30.00, 90.00)
}

# --- Geração de Dados ---

# 1. Datas Aleatórias (últimos 3 anos)
data_fim = datetime.now()
data_inicio = data_fim - timedelta(days=3 * 365)
datas = [data_inicio + (data_fim - data_inicio) * np.random.rand() for _ in range(NUM_LINHAS)]
datas_formatadas = [d.strftime('%Y-%m-%d') for d in datas]

# 2. Cod Vendas (Sequencial)
cod_vendas = np.arange(1, NUM_LINHAS + 1)

# 3. ID Loja (Escolha aleatória)
id_loja = np.random.choice(lojas, NUM_LINHAS)

# 4. Produto (Escolha aleatória)
produto_escolhido = np.random.choice(produtos, NUM_LINHAS)

# 5. Quantidade (Entre 1 e 5)
quantidade = np.random.randint(1, 6, NUM_LINHAS)

# 6. Valor Unitário (Baseado na categoria do produto)
valor_unitario = []
for prod in produto_escolhido:
    # Determina a faixa de preço com base no nome do produto
    faixa = None
    if 'Sapato' in prod: faixa = preco_min_max['Sapato']
    elif 'Tênis' in prod: faixa = preco_min_max['Tênis']
    elif 'Camisa' in prod or 'Camiseta' in prod: faixa = preco_min_max['Camisa']
    elif 'Calça' in prod: faixa = preco_min_max['Calça']
    elif 'Sapatilha' in prod: faixa = preco_min_max['Sapatilha']
    elif 'Bota' in prod: faixa = preco_min_max['Bota']
    elif 'Chinelo' in prod: faixa = preco_min_max['Chinelo']
    elif 'Blusa' in prod: faixa = preco_min_max['Blusa']
    elif 'Shorts' in prod: faixa = preco_min_max['Shorts']
    else: faixa = (50.00, 150.00) # Preço padrão se não encaixar

    # Gera um preço aleatório dentro da faixa e arredonda para duas casas
    v = np.random.uniform(faixa[0], faixa[1])
    valor_unitario.append(round(v, 2))

# 7. Valor Final (Quantidade * Valor Unitário)
valor_final = [round(q * vu, 2) for q, vu in zip(quantidade, valor_unitario)]

# --- Criação do DataFrame ---
dados = pd.DataFrame({
    'Cod Vendas': cod_vendas,
    'Data': datas_formatadas,
    'ID Loja': id_loja,
    'Produto': produto_escolhido,
    'Quantidade': quantidade,
    'Valor Unitário': valor_unitario,
    'Valor Final': valor_final
})

# --- Exportar para CSV (Opcional, mas recomendado) ---
dados.to_csv('vendas_aleatorias_93k.csv', index=False, sep=';', decimal=',')
# print(f"DataFrame criado com {NUM_LINHAS} linhas e salvo em vendas_aleatorias_93k.csv")

# --- Visualizar as primeiras linhas (apenas para conferência) ---
#print(dados.head())