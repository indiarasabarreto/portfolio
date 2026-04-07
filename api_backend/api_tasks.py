from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.post("/")
def home():
    return {"message": "API funcionando"}

@app.get("/tasks")
def list_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: str):
    tasks.append(task)
    return {"message": "Tarefa adicionada"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    tasks.pop(id)
    return {"message": "Tarefa removida"}

#run app with: uvicorn api_tasks:app --reload - http://127.0.0.1:8000/docs