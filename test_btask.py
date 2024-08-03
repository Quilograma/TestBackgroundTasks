from fastapi import FastAPI, BackgroundTasks
import asyncio
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

app = FastAPI()

def treinar_modelo():
    # Função para treinar um modelo de machine learning em segundo plano
    iris = load_iris()
    X, y = iris.data, iris.target
    modelo = RandomForestClassifier()
    modelo.fit(X, y)
    
    # Salvar o modelo treinado em um arquivo (ou armazenar em um banco de dados, etc.)
    joblib.dump(modelo, "modelo1.pkl")
    
@app.post("/treinar_modelo")
async def endpoint_treinar_modelo(background_tasks: BackgroundTasks):
    # Lançar a tarefa em background para treinar o modelo
    background_tasks.add_task(treinar_modelo)

    return {"mensagem": "Tarefa de treinamento do modelo em background foi lançada"}

@app.get("/modelo_treinado")
async def obter_modelo_treinado():
    # Carregar o modelo treinado (você pode carregá-lo de onde foi salvo)
    modelo = joblib.load("modelo1.pkl")
    return {"modelo_treinado": str(modelo)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
