# Use uma imagem base Python com Debian para mais controle de pacotes e compatibilidade
FROM python:3.9-slim

# Defina uma variável de ambiente que desabilite o buffering para melhor visualização dos logs
ENV PYTHONUNBUFFERED=1

# Configuração de diretório de trabalho
WORKDIR /app

# Copia apenas o requirements.txt (boa prática para build caching)
COPY requirements.txt /app/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação para dentro do container
COPY . /app

# Configurações de segurança e cache para o Celery
RUN adduser --disabled-password celery_user \
    && chown -R celery_user:celery_user /app \
    && mkdir -p /var/log/celery /var/run/celery \
    && chown -R celery_user:celery_user /var/log/celery /var/run/celery

# Usuário de execução do Celery para segurança
USER celery_user

# Porta padrão do Django
EXPOSE 8000

# Comando de entrada
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
