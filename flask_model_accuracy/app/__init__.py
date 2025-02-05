from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configuration can be added here if needed
    from .routes import main  # Import the routes after app creation
    app.register_blueprint(main)  # Register the blueprint
    return app