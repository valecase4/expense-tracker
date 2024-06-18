from flask import Flask, render_template, request, flash, redirect, url_for

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] ='randomsupersafekey'

    from .forms import LoginForm

    @app.route('/', methods=['GET', 'POST'])
    def index():
        login_form = LoginForm()
        
        if login_form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')

            if username == 'admin' and password == 'password':
                return redirect(url_for('homepage'))
            else:
                flash('Invalid credentials')
            
        return render_template('index.html', form=login_form)
    
    @app.route('/homepage')
    def homepage():
        return render_template('homepage.html')

    return app