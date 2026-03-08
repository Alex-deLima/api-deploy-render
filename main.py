from fastapi import FastAPI, Header, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")

def verificar_chave(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Acesso não autorizado")

@app.get("/")
def root(x_api_key: str = Header(None)):
    verificar_chave(x_api_key)
    return {"message": "Active Application API", "version": 1.0}

@app.get("/saude")
def saude(x_api_key: str = Header(None)):
    verificar_chave(x_api_key)
    return {"status": "saudavel"}


