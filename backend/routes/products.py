from flask import Blueprint, request, jsonify
from database import get_connection
from psycopg2.extras import RealDictCursor

products = Blueprint("products", __name__)

@products.route("/", methods=["GET"])
def get_products():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("SELECT * FROM products ORDER BY id ASC")
    product_list = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(product_list)


@products.route("/", methods=["POST"])
def add_product():
    data = request.json

    name = data["name"]
    price = data["price"]
    quantity = data["quantity"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO products (name, price, quantity)
        VALUES (%s, %s, %s)
        RETURNING *
        """,
        (name, price, quantity)
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message": "Product added successfully"
    })


@products.route("/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.json

    name = data["name"]
    price = data["price"]
    quantity = data["quantity"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE products
        SET name=%s, price=%s, quantity=%s
        WHERE id=%s
        """,
        (name, price, quantity, id)
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message": "Product updated successfully"
    })


@products.route("/count", methods=["GET"])
def get_product_count():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("SELECT COUNT(*) AS total_products FROM products")

    result = cur.fetchone()

    cur.close()
    conn.close()

    return jsonify(result)


@products.route("/summary", methods=["GET"])
def get_product_summary():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        SELECT
            COUNT(*) AS total_products,
            SUM(quantity) AS total_quantity
        FROM products
        """
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    return jsonify(result)