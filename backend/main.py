from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Projeto Pipeline Web")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/")
def root():
    return {"message": "API rodando com sucesso!"}