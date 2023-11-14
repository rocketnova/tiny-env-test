import logging
import os

from flask import Flask

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

def main():
    host = os.environ.get("HOST")
    port = os.environ.get("PORT")
    logger.info("Running Flask app on host %s and port %s", host, port)
    app.run(host=host, port=port)


@app.route("/")
def hello_world():
    custom_env_var = os.environ.get("CUSTOM_ENV_VAR")
    custom_secret = os.environ.get("CUSTOM_SECRET")
    return f"<p>Hello, World!</p><p>Custom env var: {custom_env_var}</p><p>Custom secret: {custom_secret}"


@app.route("/customhealth")
def health():
    return "OK"


if __name__ == "__main__":
    main()
