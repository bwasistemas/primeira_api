from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"mensagem": "API está no ar"}

@app.get("/alo")
async def alo():
    return {"mensagem": "Alô Mundo"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
