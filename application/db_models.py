import hashlib

from flask_login import UserMixin

from application import appDB, login_manager


# < tables > \\\\\\\\\\\\\\
# Таблицы базы данных
class Users(appDB.Model, UserMixin):
    __tablename__ = 'users'
    # Столбцы
    id = appDB.Column(appDB.Integer(), primary_key=True)
    login = appDB.Column(appDB.String(35), nullable=False, unique=True)
    password = appDB.Column(appDB.String(64), nullable=False)
    email = appDB.Column(appDB.String(128), nullable=True, unique=True)
    rights = appDB.Column(appDB.Integer(), nullable=False)
    name = appDB.Column(appDB.String(35), nullable=False)
    lastname = appDB.Column(appDB.String(35), nullable=False)
    middlename = appDB.Column(appDB.String(35), nullable=False)
    # Связь с таблицами
    workshops_owner = appDB.relationship('Workshops', backref='workshops_owner')
    activity_owner = appDB.relationship('Activity', backref='activity_owner')


class Workshops(appDB.Model):
    __tablename__ = 'workshops'
    # Столбцы
    id = appDB.Column(appDB.Integer(), primary_key=True)
    title = appDB.Column(appDB.String(35), nullable=False)
    description = appDB.Column(appDB.String(250), nullable=True)
    owner = appDB.Column(appDB.Integer(), appDB.ForeignKey('users.id'), nullable=True)
    kabinet = appDB.Column(appDB.String(4), nullable=False)
    # Связь
    activity_workshop = appDB.relationship('Activity', backref='activity_workshop')


class TypeActivity(appDB.Model):
    __tablename__ = 'type_activity'
    # Столбцы
    id = appDB.Column(appDB.Integer(), primary_key=True)
    title = appDB.Column(appDB.String(35), nullable=False)
    description = appDB.Column(appDB.String(250), nullable=True)
    # Связь
    activity_type_activity = appDB.relationship('Activity', backref='activity_type_activity')


class TimeInterval(appDB.Model):
    __tablename__ = 'time_interval'
    # Столбцы
    id = appDB.Column(appDB.Integer(), primary_key=True)
    title = appDB.Column(appDB.String(35), nullable=False)
    time_start = appDB.Column(appDB.DateTime(), nullable=False)
    time_end = appDB.Column(appDB.DateTime(), nullable=False)
    # Связь
    activity_time_interval = appDB.relationship('Activity', backref='activity_time_interval')


class Activity(appDB.Model):
    __tablename__ = 'activity'
    # Столбцы
    id = appDB.Column(appDB.Integer(), primary_key=True)
    type_activity = appDB.Column(appDB.Integer(), appDB.ForeignKey('type_activity.id'), nullable=False)
    time_interval = appDB.Column(appDB.Integer(), appDB.ForeignKey('time_interval.id'), nullable=False)
    date = appDB.Column(appDB.Date(), nullable=False)
    workshop = appDB.Column(appDB.Integer(), appDB.ForeignKey('workshops.id'), nullable=False)
    title = appDB.Column(appDB.String(35), nullable=False)
    description = appDB.Column(appDB.String(250), nullable=True)
    owner = appDB.Column(appDB.Integer(), appDB.ForeignKey('users.id'), nullable=False)
    status = appDB.Column(appDB.Integer(), nullable=False)


# < /tables > //////////////

# < function > \\\\\\\\\\\\\\
# Дополнительные функции
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


def generate_password_hash(password):  # Создаёт хэш пароля
    return hashlib.sha3_512(bytes(password, encoding='utf-8')).hexdigest()


def check_password_hash(password_hash, password):  # Сравнивает пароли
    if password_hash == generate_password_hash(password):
        return True
    else:
        return False
# < /function > //////////////
