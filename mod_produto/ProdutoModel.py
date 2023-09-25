import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer

# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    grupo = Column(VARCHAR(100), nullable=False)

    def __init__(self, id_produto, nome, grupo):
        self.id_produto = id_produto
        self.nome = nome
        self.grupo = grupo