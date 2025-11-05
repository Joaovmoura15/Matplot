import matplotlib.pyplot as plt
# 4. Gráfico de Dispersão
precos = [50, 120, 300, 80, 20]
estoque = [80, 25, 10, 70, 150]

plt.figure()
plt.scatter(precos, estoque)
plt.title("Relação entre Preço e Quantidade em Estoque")
plt.xlabel("Preço Unitário")
plt.ylabel("Quantidade em Estoque")
plt.show()
