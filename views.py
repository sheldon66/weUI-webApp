from forms import AddProfileForm

from functools import wraps
from flask import Flask, flash, redirect, render_template,\
                  request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

# config
app = Flask(__name__)
app.config.from_object('_config')
db = SQLAlchemy(app)

from models import Profile

@app.route('/', methods=['GET', 'POST'])
def new_profile():
    form = AddProfileForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_profile = Profile(
                form.name.data,
                form.ID_number.data,
                form.phone_number.data,
                form.work.data,
                form.degree.data
            )
            db.session.add(new_profile)
            db.session.commit()
            flash('Your profile have committed successfully.')
    return render_template('profile.html',
                            form = AddProfileForm(request.form))
