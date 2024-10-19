FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

ENV PYTHONPATH="${PYTHONPATH}:/app"

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
