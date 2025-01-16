from flask import Blueprint, jsonify
from app.utils.decorators import role_required
from app.models.user import User
from flask import g

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/profile", methods=["GET"])
@role_required(["Admin", "User"])
def profile():
    """
    Get user profile
    ---
    tags:
      - User
    security:
      - Authorization : Bearer: {token}
    responses:
      200:
        description: User profile data
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "User profile data"
      403:
        description: Unauthorized
    """

    user = User.query.filter_by(id=g.user_id).first()
    # Extract business IDs from the user object
    businesses = [{"id": business.id, "name": business.name} for business in user.businesses]
    if user: 
        return jsonify({ 
        "id": user.id,
        "first_name": user.username,
        "last_name": user.username,
        "email": user.email, 
        "role": user.role.name, 
        "businesses": businesses
        }), 200

    return jsonify({"error": "Invalid credentials"}), 401
