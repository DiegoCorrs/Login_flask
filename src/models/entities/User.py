from werkzeug.security import check_password_hash #generate_password_hash #(esto se creo solo para generar una contraseña)
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, username, password, fullname="") -> None: #sirve para manejar las entidades de tipo usuario y realizar la autenticación
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname


    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

#hashed_password = generate_password_hash("holamundo") #esto se creo solo para generar una contraseña
#print(hashed_password)
