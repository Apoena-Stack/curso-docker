
#reduzindo superficie de ataque
FROM python:3.10-slim

#Atualizações e Limpeza de cache

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libc-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Utilização de usuarios não privilegiados
   
RUN groupadd -r groupuser && useradd -r -g groupuser myuser
USER myuser

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
