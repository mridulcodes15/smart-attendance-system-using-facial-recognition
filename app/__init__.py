from flask import Flask
from .models.db import init_db
from .routes.auth_routes import auth_bp
from .routes.dashboard_routes import dashboard_bp
from .routes.attendance_routes import attendance_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "hackathon_secret"

    init_db()

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(attendance_bp)

    return app