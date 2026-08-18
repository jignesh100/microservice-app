from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "ordersdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )


@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "Running"
    })


@app.route("/health")
def health():
    try:
        conn = get_connection()
        conn.close()

        return jsonify({
            "status": "healthy",
            "database": "connected"
        })

    except Exception as e:

        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500


@app.route("/orders")
def get_orders():

    try:

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
            SELECT id,user_name,product,quantity
            FROM orders
            ORDER BY id;
        """)

        rows = cur.fetchall()

        orders = []

        for row in rows:

            orders.append({
                "id": row[0],
                "user": row[1],
                "product": row[2],
                "quantity": row[3]
            })

        cur.close()
        conn.close()

        return jsonify(orders)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)