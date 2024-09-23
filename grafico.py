
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

# Dados fornecidos
data = {
    'Data Admissão': [
        '12/07/2024', '11/07/2024', '16/07/2024', '18/07/2024', '18/07/2024', '08/08/2024', '20/08/2024', '01/07/2024', 
        '01/07/2024', '01/07/2024', '01/07/2024', '01/07/2024', '11/07/2024', '11/07/2024', '11/07/2024', '11/07/2024', 
        '11/07/2024', '12/07/2024', '12/07/2024', '12/07/2024', '12/07/2024', '23/07/2024', '25/07/2024', '25/07/2024', 
        '25/07/2024', '25/07/2024', '25/07/2024', '25/07/2024', '02/08/2024', '08/08/2024', '08/08/2024', '08/08/2024', 
        '08/08/2024', '08/08/2024', '08/08/2024', '08/08/2024', '10/08/2024', '10/08/2024', '10/08/2024', '16/08/2024', 
        '16/08/2024', '16/08/2024', '20/08/2024', '20/08/2024', '26/08/2024', '26/08/2024', '26/08/2024', '26/08/2024', 
        '29/08/2024'
    ],
    'Código Cargo': [
        455, 989, 455, 452, 455, 1386, 455, 455, 422, 1, 455, 455, 1386, 989, 505, 452, 989, 989, 422, 455, 455, 1306, 
        1386, 1386, 516, 476, 476, 476, 516, 1386, 613, 1386, 455, 1332, 989, 1386, 396, 596, 1386, 1294, 455, 455, 455, 
        396, 396, 455, 455, 455, 455
    ],
    'Cargo': [
        'AUXILIAR DE LOJA II', 'FISCAL DE PREV DE PERDAS', 'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA I', 'AUXILIAR DE LOJA II',
        'REPOSITOR', 'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA II', 'AUXILIAR DE DEPOSITO', 'ACOUGUEIRO', 'AUXILIAR DE LOJA II',
        'AUXILIAR DE LOJA II', 'REPOSITOR', 'FISCAL DE PREV DE PERDAS', 'AUXILIAR ESTACIONAMENTO', 'AUXILIAR DE LOJA I',
        'FISCAL DE PREV DE PERDAS', 'FISCAL DE PREV DE PERDAS', 'AUXILIAR DE DEPOSITO', 'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA II',
        'OPERADOR DE EMPILHADEIRA', 'REPOSITOR', 'REPOSITOR', 'BALCONISTA', 'AUXILIAR DE PRODUCAO', 'AUXILIAR DE PRODUCAO',
        'AUXILIAR DE PRODUCAO', 'BALCONISTA', 'REPOSITOR', 'CONSULTOR DE VENDA - COMISSIONADO', 'REPOSITOR', 'AUXILIAR DE LOJA II',
        'PEIXEIRO', 'FISCAL DE PREV DE PERDAS', 'REPOSITOR', 'AUXILIAR DE ACOUGUE', 'CONFERENTE', 'REPOSITOR', 'NUTRICIONISTA',
        'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA II', 'AUXILIAR DE ACOUGUE', 'AUXILIAR DE ACOUGUE',
        'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA II'
    ]
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Contagem dos cargos
cargo_counts = Counter(df['Cargo'])

# Gerando o gráfico
plt.figure(figsize=(10, 6))  
plt.bar(cargo_counts.keys(), cargo_counts.values(), color='skyblue')
plt.xticks(rotation=90)
plt.title('Distribuição de Admissões por Cargo')
plt.xlabel('Cargo')
plt.ylabel('Número de Admissões')
plt.tight_layout()

# Exibir o gráfico
plt.show()

