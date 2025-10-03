FROM python:3.13.5-alpine3.22

RUN apk add --no-cache postgresql-dev gcc musl-dev
COPY ./src/requirements.txt /home/app/requirements.txt
RUN chmod a+r /home/app/requirements.txt
RUN pip install -r /home/app/requirements.txt

WORKDIR /home/app/src

# CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "main_fastapi.py"]
# CMD ["python", "main.py"]
# docker compose exec consola python -m debugpy --listen 0.0.0.0:5678 app.py
# python -m debugpy --listen 0.0.0.0:5678 main_fastapi.py