FROM python:3.10

WORKDIR /app

RUN mkdir -p /app/data

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./iss_tracker.py .

CMD ["python", "iss_tracker.py"]