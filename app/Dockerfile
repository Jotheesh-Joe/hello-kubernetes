FROM python:3.9-slim

LABEL maintainer="Jotheeswaran Lakshmanan"

WORKDIR /app

COPY app/requirements.txt /app

COPY app/app.py /app

COPY app/static /app/static

COPY app/templates /app/templates

RUN pip install -r ./requirements.txt

CMD ["python", "-u", "./app.py"]
