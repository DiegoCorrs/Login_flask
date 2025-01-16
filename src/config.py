from datetime import timedelta

class Config:
    SECRET_KEY = 'B!1weNAtiT^%kvhUI*S^' #sirve para enviar mensajes atraves de la función flash propia de flask

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'flask_login'
    SESSION_PERMANENT = False  # Las sesiones estándar no son permanentes
    REMEMBER_COOKIE_DURATION = timedelta(days=7)  # Duración de la cookie "Remember me"

config={
    'development':DevelopmentConfig
}


