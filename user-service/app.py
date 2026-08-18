from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL", "http://order-service:5001")


@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "status": "Running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/users")
def users():

    user_data = [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com"
        },
        {
            "id": 2,
            "name": "Alice",
            "email": "alice@example.com"
        }
    ]

    return jsonify(user_data)


@app.route("/user-orders")
def user_orders():
    """
    Demonstrates service-to-service communication.
    User Service calls Order Service.
    """

    try:
        response = requests.get(f"{ORDER_SERVICE_URL}/orders", timeout=5)

        return jsonify({
            "user": "John Doe",
            "orders": response.json()
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)