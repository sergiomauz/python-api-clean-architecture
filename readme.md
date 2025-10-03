# Microservicios Python

## Para ejecutar

- Primero debe ejecutarse **docker compose up -d** para correr los contenedores necesarios.
- Luego, para entrar al programa de la consola, ejecutar:
  **docker exec -it <ID_CONTAINER> sh**
  **python -m debugpy --listen 0.0.0.0:5678 main_flask.py**
  **python -m debugpy --listen 0.0.0.0:5678 main_fastapi.py**
  