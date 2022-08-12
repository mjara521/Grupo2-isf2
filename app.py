from re import U
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from db import poolDataBase
from werkzeug.security import check_password_hash
import psycopg2
import psycopg2.extras

# Inicio de sesión de usuario, cierre de sesión de usuario, vista de usuario;
app = Flask(__name__)
app.secret_key = 'password123456'
bootstrap = Bootstrap(app)

@app.route('/')
def inicio():
    return render_template('login.html')
    #return render_template('loginTest.html')
    
@app.route('/menu_principal')
def menu_principal():
    return render_template('menu_principal.html')

@app.route('/modulo_seguridad')
def modulo_seguridad():
    return render_template('modulo_seguridad.html')

@app.route('/modulo_proyecto')
def modulo_proyecto():
    return render_template('modulo_proyecto.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    #cursor = poolDataBase.getCursorSgp()

    # Comprueba si el usuario, la contrasenha o  el email ya existe en la base de datos
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(password)
        print(username)
        
        # Por ahora para esta parte de la entrega colocamos estos valores hardcode
        usuario = 'admin'
        contraseña = 'admin'

        if username==usuario and password==contraseña:
            # Se redirecciona
            return redirect(url_for('menu_principal'))
        else:
            # Cuenta no existe o usuario/contraseña incorrecta
            flash('Usuario o contraseña errónea')
            return redirect(url_for('inicio'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

