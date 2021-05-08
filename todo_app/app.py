from flask import Flask
from flask_login import current_user

from todo_app.extensions import login_manager, db, migrate
from todo_app.models import User


def register_blueprints(app: Flask):
    from todo_app.views import main, auth

    app.register_blueprint(main.routes)
    app.register_blueprint(auth.routes)


def register_extensions(app: Flask):
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_flask_login_configs():
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'alert-info'


def create_app(config_object='todo_app.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_blueprints(app)
    register_extensions(app)
    register_flask_login_configs()

    # Make utils available in any Flask template.
    @app.context_processor
    def inject_utils():
        return dict(user=current_user)

    return app
