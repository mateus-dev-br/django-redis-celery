# Use uma imagem base leve
FROM python:3.9-slim

# Desabilita o buffering para melhor visualização de logs
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho
WORKDIR /app

# Copia apenas o requirements.txt (boa prática para build caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Instala o Gunicorn para Django e Celery para tarefas assíncronas
RUN pip install gunicorn

# Copia o código da aplicação
COPY . /app

# Cria usuários sem privilégios para maior segurança
RUN adduser --disabled-password appuser \
    && adduser --disabled-password celery_user \
    && chown -R appuser:appuser /app \
    && mkdir -p /var/log/gunicorn /var/run/gunicorn /var/log/celery /var/run/celery \
    && chown -R appuser:appuser /var/log/gunicorn /var/run/gunicorn \
    && chown -R celery_user:celery_user /var/log/celery /var/run/celery

# Usa o usuário sem privilégios para rodar o Gunicorn
USER appuser

# Expõe a porta 8000 para o Gunicorn
EXPOSE 8000

# Comando de entrada para o Gunicorn (será sobrescrito para o Celery no docker-compose)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application", "--workers", "4", "--timeout", "120"]
