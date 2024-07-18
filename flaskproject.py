from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name":  "John 'EL PLAN' de Dios Pantoja",
        "email": "john.doe@example.com",
        "age": 18,
        "country": "UK",
        "email2": "john.doe@example.de",
        "age": 18,
        "country": "UK",
    }
    user_country = {
        "countryy": "DE",
        "user_id": user_id,
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200
    return jsonify(user_country), 200
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
