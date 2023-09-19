from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    descricao: int = str
    valor_unitario: float
    foto: bytes