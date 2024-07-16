FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -r appuser && useradd -r -g appuser appuser && \
    mkdir -p /home/appuser && chown -R appuser:appuser /home/appuser 

USER appuser

CMD ["python", "app.py"]