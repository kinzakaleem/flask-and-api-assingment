from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data: list of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob",   "email": "bob@example.com"},
    {"id": 3, "name": "Carol", "email": "carol@example.com"}
]

@app.route('/')
def home():
    return "<h1>Flask JSON API Example</h1><p>Go to /api/users to see JSON data.</p>"

@app.route('/api/users', methods=['GET'])
def get_users():
    # Return the full list of users as JSON
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Find the user with the matching id
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def add_user():
    # Expect JSON body with "name" and "email"
    new_data = request.get_json()
    if not new_data or not all(k in new_data for k in ("name", "email")):
        return jsonify({"error": "Invalid request"}), 400

    new_id = max(u["id"] for u in users) + 1
    new_user = {"id": new_id, "name": new_data["name"], "email": new_data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)