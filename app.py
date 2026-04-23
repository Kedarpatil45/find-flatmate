from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    return jsonify({"message": "Login successful"})

@app.route("/user", methods=["POST"])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added", "user": data})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)