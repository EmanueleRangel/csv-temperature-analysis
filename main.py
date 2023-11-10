import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


dados = pd.read_csv('dados.csv')

print(dados.columns)
media = dados["temperatura"].mean()
desvio_padrao = dados["temperatura"].std()
maximo = dados["temperatura"].max()
minimo = dados["temperatura"].min()


if 'temperatura' in dados.columns:
    media = dados['temperatura'].mean()
    print("Média: ",media)

    print("Desvio padrão: ",desvio_padrao)

    print("Máximo: ",maximo)

    print("Mínimo: ",minimo)

    print("Dados da coluna: ", dados.columns)

    dados = pd.DataFrame({})

    print(dados.empty)


print(media)

print(desvio_padrao)

print(maximo)

print(minimo)

print(dados.columns)

plt.switch_backend("TkAgg")
plt.savefig("Repos personal/python_data/figure.png")

plt.show()

plt.plot(dados["data"], dados["temperatura"])
plt.show()
