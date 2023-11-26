# import da persistência
import db
from mod_produto.ProdutoModel import ProdutoDB
from fastapi import APIRouter
from mod_produto.Produto import Produto

router = APIRouter()
# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/produtos/", tags=["Produtos"])
def get_produto():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/produtos/{id}", tags=["Produtos"])
def get_produto(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()   

@router.post("/produtos/", tags=["Produtos"])
def post_produto(corpo: Produto):
    try:
        session = db.Session()

        dados = ProdutoDB(None, corpo.nome, corpo.grupo)

        session.add(dados)

        session.commit()

        return {"id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produtos/{id}", tags=["Produtos"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(
            ProdutoDB.id_produto == id).one()
        
        dados.nome = corpo.nome
        dados.grupo = corpo.grupo

        session.add(dados)
        session.commit()

        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/produtos/{id}", tags=["Produtos"])
def delete_produto(id: int):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()

        return {"id": dados.id_produto}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()