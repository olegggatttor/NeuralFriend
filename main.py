import uvicorn
from fastapi import FastAPI

from main_router import main_router

app = FastAPI(title="Neural Friend")

app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run( app='main:app')