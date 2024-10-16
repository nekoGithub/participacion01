from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = "unaclavesecreta"

usuarios = {'Brayan': 'password', 'Pedro': 'password1'}

@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        contraseña = request.form.get('contraseña')

        if nombre in usuarios and usuarios[nombre] == contraseña:
            session['usuario'] = nombre
            return redirect(url_for('home'))
        else:
            print('Nombre de usuario o contraseña incorrectos. Intenta de nuevo.')
            return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route('/home')
def home():
    if 'usuario' in session:
        return render_template('home.html', usuario = session['usuario'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)