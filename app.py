from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'nok123'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Vérifiez ici si les informations d'identification sont valides
    if username == 'admin' and password == 'password':
        user = User(user_id=1)
        login_user(user)
        return redirect(url_for('success'))
    else:
        return render_template('login.html')

@app.route('/success')
@login_required
def success():
    return "Authentification réussie !"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()