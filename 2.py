import matplotlib.pyplot as plt
# 2. Gráfico de Barras
produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam']
quantidades = [50, 75, 30, 60]

plt.figure()
plt.bar(produtos, quantidades)
plt.title("Comparação de Produtos em Estoque")
plt.xlabel("Produtos")
plt.ylabel("Quantidade")
plt.show()
