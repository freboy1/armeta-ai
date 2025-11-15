from fastapi import FastAPI
from app.routes.file_route import router as file_router


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(file_router)