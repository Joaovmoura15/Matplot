import matplotlib.pyplot as plt
# 3. Gráfico de Pizza
categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
valores = [15000, 8000, 5000]

plt.figure()
plt.pie(valores, labels=categorias, autopct='%1.1f%%')
plt.title("Proporção do Valor Total de Estoque por Categoria")
plt.show()
