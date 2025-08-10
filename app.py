from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Vidit", "email": "vidit@example.com"},
    {"id": 2, "name": "Ramesh", "email": "ramesh@example.com"}
]

@app.route('/')
def home():
    return "Hello, World"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    for user in users:
        if user["id"] == user_id:
            data = request.get_json()
            user.update(data)
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)