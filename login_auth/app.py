from flask import Flask
from routes.credentials import blp
from flask_smorest import Api

app = Flask(__name__)
app.config["PROPOGATE_EXCEPTIONS"]=True
app.config["API_TITLE"]="users API"
app.config["API_VERSION"]="v1"
app.config["OPENAPI_VERSION"]="3.0.3"
app.config["OPEN_URL_PREFIX"]="/"


api = Api(app)
api.register_blueprint(blp)

if __name__ == 'main':
    app.run(debug=True)
