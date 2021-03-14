from flask import render_template, redirect

from application import app
from application.db_models import Users, Workshops, TypeActivity, TimeInterval, Activity


@app.route('/')
def open_application():
    return redirect('/signin')
    #return render_template('index.html')
