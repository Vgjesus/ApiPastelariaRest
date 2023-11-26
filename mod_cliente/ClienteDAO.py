# import da persistência
import db
from mod_cliente.ClienteModel import ClienteDB
from fastapi import APIRouter
from mod_cliente.Cliente import Cliente

router = APIRouter()

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE

@router.get("/clientes/", tags=["Clientes"])
def get_cliente():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ClienteDB).all()
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/clientes/{id}", tags=["Clientes"])
def get_cliente(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()   

@router.post("/clientes/", tags=["Clientes"])
def post_cliente(corpo: Cliente):
    try:
        session = db.Session()

        print(corpo)

        dados = ClienteDB(None, corpo.nome, corpo.matricula, corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha)

        session.add(dados)

        session.commit()

        return {"id": dados.id_cliente}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/clientes/{id}", tags=["Clientes"])
def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()

        dados = session.query(ClienteDB).filter(
            ClienteDB.id_cliente == id).one()
        
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo

        session.add(dados)
        session.commit()

        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/clientes/{id}", tags=["Clientes"])
def delete_cliente(id: int):
    try:
        session = db.Session()

        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        session.delete(dados)
        session.commit()

        return {"id": dados.id_cliente}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()