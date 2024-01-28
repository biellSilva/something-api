from uvicorn import run

from src import app
from src.domain import config


DEBUG = True

if __name__ == "__main__":
    if DEBUG:
        run("main:app", reload=True)
    else:
        run(app=app, host=config.app_host, port=config.app_port)
