import pandas as pd

#          Cod Vendas                           Data    Quantidade  Valor Unitario   Valor Final
# count  93000.000000                          93000  93000.000000    93000.000000  93000.000000
# mean   46500.500000  2024-05-23 15:26:54.658064384      2.995925      117.613656    352.138065
# min        1.000000            2022-11-24 00:00:00      1.000000       10.000000     10.010000
# 25%    23250.750000            2023-08-24 00:00:00      2.000000       63.990000    142.320000
# 50%    46500.500000            2024-05-23 00:00:00      3.000000      101.065000    267.945000
# 75%    69750.250000            2025-02-20 00:00:00      4.000000      153.812500    474.885000
# max    93000.000000            2025-11-23 00:00:00      5.000000      349.990000   1747.950000
# std    26887.284228  NaT                                1.414251       85.486263    256.287283

#                           Quantidade  Valor Unitario   Valor Final
# count (soma dos valores)  93000
# mean (média dos valores)   117.613656
# min (valor mínimo)         10.000000
# 25% (1º quartil)          63.990000
# 50% (mediana)             101.065000
# 75% (3º quartil)          153.812500
# max (valor máximo)        349.990000
# std (desvio padrão)       85.486263

vendasArq_df = pd.read_excel('Vendas1.xlsx')
print(vendasArq_df.describe())