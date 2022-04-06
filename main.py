from fastapi import FastAPI
from pydantic import BaseModel

# Run on Terminal
# python -m venv ./venv
# .\venv\Scripts\activate.bat
# python.exe -m pip install --upgrade pip
# pip install fastapi
# pip install uvicorn
# uvicorn main:app --reload
# Enter at http://127.0.0.1:8000/docs

app = FastAPI()

@app.get('/')
def raiz():
    return {'Hello': 'World!'}

class Usuario(BaseModel):
    id: int
    email: str
    senha: str

base_de_dados = [
    Usuario(id=1, email='leonardo@leonardo.com.br', senha='12345'),
    Usuario(id=2, email='teste@teste.com.br', senha='12345')
]

@app.get('/usuarios')
def get_todos_os_usuarios():
    return base_de_dados

@app.get('/usuarios/{id_usuario}')
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
    return {'Status': 404, 'Mensagem': 'Usuário não encontrado'}

@app.post('/usuarios')
def insere_usuario(usuario: Usuario):
    base_de_dados.append(usuario)
    return usuario