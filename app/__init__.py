from flask import Flask, render_template, request, flash, redirect, url_for, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user
import werkzeug

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    login_manager = LoginManager()

    app.config['SECRET_KEY'] ='randomsupersafekey'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

    db.init_app(app)
    login_manager.init_app(app)

    from .forms import LoginForm
    from .forms import AddExpenseForm

    @app.route('/', methods=['GET', 'POST'])
    def index():
        login_form = LoginForm()
        
        if login_form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')

            admin = Admin.query.filter_by(username='admin').first()

            if admin:
                if username == admin.username and password == admin.password:
                    login_user(admin, remember=False)
                    return redirect(url_for('homepage'))
                else:
                    flash('Invalid credentials')
            else:
                abort(401)
            
        return render_template('index.html', form=login_form)
    
    @app.route('/dashboard', methods=['GET', 'POST'])
    @login_required
    def homepage():
        add_expense_form = AddExpenseForm() 
        
        if add_expense_form.validate_on_submit():
            print("Ok")

        return render_template('homepage.html', form=add_expense_form)
    
    @app.route('/<int:id>/settings')
    def settings(id):
        return f"Settings {id}"

    @app.errorhandler(werkzeug.exceptions.Unauthorized)
    def handle_unauthorized(e):
        return "Unauthorized", 401
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404
    
    from .models import Admin
    from .models import Expense
    from .models import Category
    from .models import PaymentMethod

    @login_manager.user_loader
    def load_user(id):
        return Admin.query.get(int(id))

    with app.app_context():
        admin = Admin.query.filter_by(username='admin').first()

        if not admin:
            new_admin = Admin(username='admin', password='password')
            db.session.add(new_admin)
            db.session.commit()

        db.create_all()

    return app