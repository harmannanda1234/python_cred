from flask import request
from flask.views import MethodView
from flask_smorest import blueprint 

blp = blueprint("users",__name__,description="this stores info related to users" )

@blp.route("/signup")
class Signup(MethodView):
    def post(self):
        req = request.get_json()
        if req['username'] is None or req['password'] is None :
            return {"message":"invalid req"}
        
        
    