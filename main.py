from fastapi import FastAPI
from src.projects import router as projects_router
from src.tasks import router as tasks_router

app = FastAPI()
app.include_router(projects_router)
app.include_router(tasks_router)

@app.get('/')
def read_root():
    return {"Message":"Hello from Root"}