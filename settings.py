from urllib.parse import quote # por causa do @ na senha...
from dotenv import load_dotenv, find_dotenv
import os

# localiza o arquivo de .env
dotenv_file = find_dotenv()

# Carrega o arquivo .env
load_dotenv(".env")

# Configurações da API
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")

# Configurações Segurança da API
X_TOKEN = os.getenv("X_TOKEN")
X_KEY = os.getenv("X_KEY")

# Configurações banco de dados
DB_SGDB = os.getenv("DB_SGDB")
DB_NAME = os.getenv("DB_NAME")

# Caso seja diferente de sqlite
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Ajusta STR_DATABASE conforme gerenciador escolhido
STR_DATABASE = f"sqlite:///{DB_NAME}.db"