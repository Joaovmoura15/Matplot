import matplotlib.pyplot as plt
# 1. Gráfico de Linha
dias = [1, 2, 3, 4, 5, 6, 7]
estoque_diario = [100, 95, 110, 105, 120, 115, 130]

plt.figure()
plt.plot(dias, estoque_diario)
plt.title("Tendência de Estoque Diário")
plt.xlabel("Dias")
plt.ylabel("Quantidade em Estoque")
plt.show()

