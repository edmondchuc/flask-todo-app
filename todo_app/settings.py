try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

from os import environ

# Flask
SECRET_KEY = environ.get('SECRET_KEY', 'a-very-bad-secret-key-please-use-something-else')

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///../todo.db')
