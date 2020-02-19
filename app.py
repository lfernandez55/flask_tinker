from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm #Form is deprecated, use FlaskForm instead
from wtforms import StringField, IntegerField, ValidationError, FieldList, FormField, SubmitField, HiddenField, SelectMultipleField, widgets
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/create_all')
def create_all():
    db.create_all()
    flash('DB Added!!')
    return redirect(url_for('home_page'))

@app.route('/drop_all')
def drop_all():
    db.drop_all()
    flash('DB Dropped!!')
    return redirect(url_for('home_page'))
