from flask import Flask, jsonify, render_template
from flask_cors import CORS

from database import init_db
from routes import products

init_db()

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

CORS(app, origins="*")

app.register_blueprint(products, url_prefix="/products")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "message": "Server Online"
    })


if __name__ == "__main__":
    app.run(debug=True)