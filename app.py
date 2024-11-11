#Imoort classes and functions needed to this service
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager,jwt_required, create_access_token, get_jwt_identity 

#Create an instance of Flask and a JWT secret key for the tokens and initialize JWTManager
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "cbaleman04" 
jwt = JWTManager(app)

#The route that we're using to use the method login
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "password":
        return jsonify({"msg": "Wrong username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# protected route
@app.route('/protected', methods=['GET'])
@jwt_required()  # This requires the secret token
def protected():
    # If the token is right we've get the identity of the user
    current_user = get_jwt_identity()  # get the jwt identity
    return jsonify(logged_in_as=current_user), 200

if __name__ == "__main__":
    app.run(debug=True)
