from flask import Flask
from app_routes import routes

app = Flask(__name__)
routes(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)