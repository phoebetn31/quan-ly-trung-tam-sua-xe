from flask import Flask
from pathlib import Path

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["EMPLOYEE_DATA_PATH"] = str(Path(app.instance_path) / "nhanvien.json")
    from app.routes.auth import bp as auth_bp
    from app.routes.admin import bp as admin_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    return app
