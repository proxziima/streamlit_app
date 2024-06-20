# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de requisitos e instalar dependências
COPY docker/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Baixar o modelo SpaCy necessário
RUN python -m spacy download pt_core_news_md

# Copiar o restante do código para o contêiner
COPY . .

# Definir o PYTHONPATH
ENV PYTHONPATH=/app

# Comando para rodar a aplicação
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
