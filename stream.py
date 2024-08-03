from fastapi import FastAPI
import time
import asyncio

from sklearn.datasets import load_iris, load_diabetes
import pandas as pd

# Função assíncrona para ler o primeiro dataset e aplicar uma transformação
async def ler_dataset1_e_aplicar_transformacao():
    # Carregar o conjunto de dados Iris
    iris_data = load_iris()

    # Converter os dados do conjunto de dados em um DataFrame Pandas
    dataset1 = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

    async for i in range(100000):
        resultado = await str(i)
        print("função 2: "+ resultado)
    # Aplicar uma transformação (por exemplo, obter as primeiras 5 linhas)
    dataset1_transformado = dataset1.head()

    return dataset1_transformado

# Função assíncrona para ler o segundo dataset e aplicar uma transformação
async def ler_dataset2_e_aplicar_transformacao():
    # Carregar o conjunto de dados Diabetes
    diabetes_data = load_diabetes()

    async for i in range(100000):
        resultado = await str(i)
        print("função 2: "+ resultado)

    # Converter os dados do conjunto de dados em um DataFrame Pandas
    dataset2 = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)

    # Aplicar uma transformação (por exemplo, obter as últimas 5 linhas)
    dataset2_transformado = dataset2.tail()

    return dataset2_transformado

app = FastAPI()

base_de_dados_usuarios = {
    1: {"id": 1, "nome": "Alice", "idade": 30, "email": "alice@example.com"},
    2: {"id": 2, "nome": "Bob", "idade": 25, "email": "bob@example.com"},
    3: {"id": 3, "nome": "Carol", "idade": 35, "email": "carol@example.com"},
    4: {"id": 4, "nome": "David", "idade": 28, "email": "david@example.com"},
}

base_de_dados_produtos = {
    101: {"id": 101, "nome": "Produto A", "preco": 20.0, "estoque": 100},
    102: {"id": 102, "nome": "Produto B", "preco": 15.0, "estoque": 75},
    103: {"id": 103, "nome": "Produto C", "preco": 30.0, "estoque": 50},
    104: {"id": 104, "nome": "Produto D", "preco": 25.0, "estoque": 90},
}


async def get_usuarios():
    await asyncio.sleep(2)
    return base_de_dados_usuarios

async def get_produtos():
    await asyncio.sleep(2)
    return base_de_dados_produtos


async def fun1():
    await asyncio.sleep(1)  # Simulando uma operação assíncrona
    return "Resultado da função 1"

async def fun2():
    await asyncio.sleep(2)  # Simulando outra operação assíncrona
    return "Resultado da função 2"


async def fun3():
    futures = [fun1(), fun2()]
    resultado1,resultado2 = await asyncio.gather(*futures)
    resultado3 = f"Resultado da função 3 com {resultado1} e {resultado2}"
    return resultado3

@app.get("/executar_funcoes")
async def executar_funcoes():
    start = time.time()
    resultado = await fun3()
    dataset1 = await ler_dataset1_e_aplicar_transformacao()
    dataset2 = await ler_dataset2_e_aplicar_transformacao()
    end = time.time()
    return {"resultado_final": resultado, "tempo": end -start, 'data1': dataset1, 'data2': dataset2}


@app.get("/get_async")
async def root():
    """
    my home route
    """
    start = time.time()
    """
    
    futures = [get_produtos_asinc(), get_usuarios_asinc()]
    produtos,usuarios = await asyncio.gather(*futures)
    """
    futures = [get_produtos(), get_usuarios()]
    produtos,usuarios = await asyncio.gather(*futures)
    end = time.time()
    print('It took {} seconds to finish execution.'.format(round(end-start)))

    return {
        'a': produtos,
        'b': usuarios
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
