from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
import werkzeug
import werkzeug.exceptions

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] ='randomsupersafekey'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

    db.init_app(app)

    from .forms import LoginForm

    @app.route('/', methods=['GET', 'POST'])
    def index():
        login_form = LoginForm()
        
        if login_form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')

            admin = Admin.query.filter_by(username='admin').first()

            if admin:
                if username == admin.username and password == admin.password:
                    return redirect(url_for('homepage'))
                else:
                    flash('Invalid credentials')
            else:
                abort(401)
            
        return render_template('index.html', form=login_form)
    
    @app.route('/homepage')
    def homepage():
        return render_template('homepage.html')

    @app.errorhandler(werkzeug.exceptions.Unauthorized)
    def handle_unauthorized(e):
        return "Unauthorized", 401
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404
    
    from .models import Admin

    with app.app_context():
        admin = Admin.query.filter_by(username='admin').first()

        if not admin:
            new_admin = Admin(username='admin', password='password')
            db.session.add(new_admin)
            db.session.commit()

        db.create_all()

    return app