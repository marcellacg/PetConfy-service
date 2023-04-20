from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.usuario import Usuario

from helpers.database import db, migrate

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://marcella:409014@localhost:5432/petconfy-service"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)

api.add_resource(Usuario, '/usuarios')

if __name__ == '__main__':
    app.run(debug=True)

