from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key-change-me'
app.config['JWT_SECRET_KEY'] = 'jwt-super-secret-key-change-me'

# Basic Authentication setup
basic_auth = HTTPBasicAuth()

# In-memory user store: username -> {username, password_hash, role}
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@basic_auth.verify_password
def verify_basic(username, password):
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return False
    return username

@app.route('/basic-protected')
@basic_auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT setup
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Bad credentials"}), 401
    # Embed role into token
    additional_claims = {"role": user['role']}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt_identity()  # identity is username
    token_data = request.headers.get('Authorization', '')
    from flask_jwt_extended import get_jwt
    claims = get_jwt()
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Custom error handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized(err_msg):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid(err_msg):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_fresh_required():
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
