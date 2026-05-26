from flask import Flask, jsonify
from flask_cors import CORS

from database import init_db
from routes import products

init_db()

app = Flask(__name__)

CORS(app, origins="*")

app.register_blueprint(products, url_prefix="/products")


@app.route("/")
def home():
    return jsonify({
        "message": "Server Online"
    })


if __name__ == "__main__":
    app.run(debug=True)