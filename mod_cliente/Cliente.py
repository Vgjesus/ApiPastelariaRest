from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    grupo: int
    senha: str = None