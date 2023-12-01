FROM python:3.9-slim

LABEL maintainer="Jotheeswaran Lakshmanan"

WORKDIR /app

Copy app/requirements.txt /app

Copy app/app.py /app

RUN pip install -r ./requirements.txt

RUN useradd -r -u 5500 appuser

RUN chown -R appuser:appuser /app

USER 5500

CMD ["python", "-u", "./app.py"]