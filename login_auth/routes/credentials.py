from flask import request , jsonify
from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint("users",__name__,description="this stores info related to users" )

@blp.route("/signup")
class Signup(MethodView):
    def post(self):
        req = request.get_json()
        username = req['username']
        passwd= req['password']
        if not username  or not passwd:
            return jsonify({"message":"invalid req"})
        
        
        
        
        
    