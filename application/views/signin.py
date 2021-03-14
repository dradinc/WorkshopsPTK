from flask import render_template, request, url_for
from flask_login import login_user, current_user

from application import app, appDB
from application.db_models import Users, Workshops, TypeActivity, TimeInterval, Activity


@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    if request.method == 'GET':
        return render_template('signin.html', login='')
