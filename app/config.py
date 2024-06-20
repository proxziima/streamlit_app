import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define as variáveis de configuração
SPACY_MODEL = os.getenv('SPACY_MODEL', 'pt_core_news_md')
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './data/uploads')
SIMILARITY_THRESHOLD = float(os.getenv('SIMILARITY_THRESHOLD', 0.90))
