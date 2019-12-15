from flask import Flask, render_template, session, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfh723809fog2o3h2cw'

    Bootstrap(app)

    return app

app = create_app()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Email(message="Username has to be in the form of email")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="Password has to be 8 characters or longer!")])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for('login'))
    return render_template('index.html', form=form, username=session.get('username'));

@app.route('/o-nama')
def o_nama():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for('login'))
    return render_template('o-nama.html', form=form, username=session.get('username'));

@app.route('/kontakt')
def kontakt():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for('login'))
    return render_template('kontakt.html', form=form, username=session.get('username'))

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for('login'))
    return render_template('login.html', form=form, username=session.get('username'))

@app.route('/#usluge')
def usluge():
    return render_template('index.html#usluge');

@app.route('/#meni')
def meni():
    return render_template('index.html#meni');

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html');