import logging
from flask import Flask
from logging.config import dictConfig

app = Flask(__name__)

dictConfig({
    "version": 1,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"}
    },
    "root": {"handlers": ["console"], "level": "INFO"},
})

@app.route('/hello')
def hello():
    app.logger.info('hello() function was called')
    return "Hello, world!"

if __name__ == '__main__':
    app.run()