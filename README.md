# Flask Login

Este es un proyecto de ejemplo que implementa un sistema de autenticación de usuarios con Flask. Utiliza Flask-Login para la gestión de sesiones, incluye la funcionalidad de "Remember Me" y una base de datos MySQL para almacenar usuarios.

## Características

- Registro de usuarios.
- Inicio de sesión con autenticación de contraseñas.
- Funcionalidad de "Remember Me" para mantener la sesión activa.
- Rutas protegidas solo accesibles para usuarios autenticados.
- Manejador de errores para 401 (No autorizado) y 404 (Página no encontrada).
  
## Requisitos

- Python 3.7 o superior
- MySQL o MariaDB
- pip (gestor de paquetes de Python)

## Librerías requeridas

- Flask
- Flask-MySQLdb
- Flask-WTF (para protección CSRF)
- Flask-Login

## Seguridad

Este proyecto utiliza Flask-WTF para la protección contra ataques CSRF y Flask-Login para la autenticación de usuarios. Se debe cambiar la clave secreta (SECRET_KEY) para mejorar la seguridad de las sesiones.

## Capturas

![image](https://github.com/user-attachments/assets/eb25a4c3-991f-48ba-9c59-458c5f245ef9)

### Mensajes de error

![image](https://github.com/user-attachments/assets/9151a981-3832-4efc-a05f-4ea86081332d) ![image](https://github.com/user-attachments/assets/c515133f-4a0e-4ad8-986c-8904f124d7b7)


## /home

![image](https://github.com/user-attachments/assets/b474e66d-5d3b-46bc-ac34-150f03d2c207)


## /protected

![image](https://github.com/user-attachments/assets/bf2dd933-7a6c-40f4-a858-efe93fa4cda6)

## Base de datos

![image](https://github.com/user-attachments/assets/a6a93c3f-ece1-4696-8556-b04bba8f3fe8)










