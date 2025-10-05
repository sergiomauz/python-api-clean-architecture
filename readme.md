# FastAPI/Flask Restful API using Clean Architecture: Warehouse

>This project implements a backend which can manage a simple Inventory of products in a warehouse, with categories, products, partners (suppliers and customers) and movements.

## Screenshots

![screenshot-1](https://i.imgur.com/ju1sXNt.png)

## Built With

- Visual Studio Code
- Docker and Docker Compose
- Python 3.13
- FastAPI / Flask
- Uvicorn
- Restful APIs
- Swagger for API documentation
- SQL Alchemy
- Dependency Injector
- DebugPy
- Alembic

## Used Techniques

- Clean architecture
- Clean code
- Dependency injection
- Serializing and deserializing objects
- Asynchronous tasks
- JSON and dynamic objects
- Lambda expressions
- Handling exceptions
- Integer and GUID identifiers

## Class Diagram

![screenshot-2](https://i.imgur.com/UAtHHVI.png)

## How to Install

- Install Visual Studio Code in your computer.
- Install Docker Desktop in your computer.
- Clone this repository using **git clone**.
- Run docker compose file: **``docker compose up -d --build --force-recreate``**
- Go to terminal of this container **"warehouse_inventory_api"**, for example using this command for this ID 2db86c41f0f7: **``docker exec -it 2db86c41f0f7 sh``**
- In the the terminal of **"warehouse_inventory_api"** run migrations using Alembic. To get all available Alembic commands run **``python main_db_migrations.py help``**, and to understand them, go to [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/).
- To run the last migration: **``python main_db_migrations.py upgrade head``**
- Make sure the tables were created using PgAdmin. Password: 711703
- To run microservice with FastAPI: **``python -m debugpy --listen 0.0.0.0:5678 main_fastapi.py``**
- To run microservice with Flask: **``python -m debugpy --listen 0.0.0.0:5678 main_flask.py``**
- Install extensions for VS Code: "Mono Kai Pro", "Python Indent", "Python Envinronments", "Pylance", "Python", "Python Debugger" and "Dev Containers".
- Open VS Code with a remote connection to Docker, attaching container **"warehouse_inventory_api"**.
- After running microservice (FastAPI or Flask), to start debugging mode, in VS Code press **F5** and set breakpoints in the code.
- Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to verify that the microservice is running. You can use endpoints with the client of your preference.

## Author

**Sergio Zambrano** 👤

- GitHub: [@sergiomauz](https://github.com/sergiomauz)
- X: [@sergiomauz](https://x.com/sergiomauz)
- Linkedin: [Sergio Zambrano](https://www.linkedin.com/in/sergiomauz/)

## Contributing 🤝

Contributions, issues and feature requests are welcome!. Feel free to check the [issues page](../../issues/).

## Show me your support

- Give a ⭐️ if you like this project.
- If you found this project helpful and would like to buy me a coffee, you can do so using Paypal:

[![Donar con PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?business=sergio.mauz88@gmail.com&currency_code=USD)

## License 📝

This project is [MIT](./LICENSE) licensed.
