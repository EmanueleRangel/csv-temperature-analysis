import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI


import pandas as pd

dados = pd.DataFrame({
    "temperatura": [10.0, 20.0, 30.0, 40.0]
})

dados = dados.assign(data=[30.0, 5.0, 35, 25])

plt.switch_backend("TkAgg")

plt.plot(dados["data"], dados["temperatura"])

plt.show()


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


app = FastAPI()

@app.get("/")
def index():
    media = dados["temperatura"].mean()
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
