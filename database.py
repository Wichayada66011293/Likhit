# database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ------------------------------
# User table
# ------------------------------
class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

# ------------------------------
# Personal Profile (1-to-1 with User)
# ------------------------------
class PersonalProfile(db.Model):
    __tablename__ = 'Personal_Profile'
    profile_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    full_name = db.Column(db.String(255))
    gender = db.Column(db.String(50))
    age = db.Column(db.Integer)

# ------------------------------
# Training (Many per User)
# ------------------------------
class Training(db.Model):
    __tablename__ = 'Training'
    training_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    picture_labeling = db.Column(db.String(255))
    sound_labeling = db.Column(db.String(255))

# ------------------------------
# Language (Many per User)
# ------------------------------
class Language(db.Model):
    __tablename__ = 'Language'
    language_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    language_type = db.Column(db.String(100))

# ------------------------------
# Work_Type (Independent)
# ------------------------------
class WorkType(db.Model):
    __tablename__ = 'Work_Type'
    work_type_id = db.Column(db.Integer, primary_key=True)
    work = db.Column(db.String(255))
    data = db.Column(db.String(255))

# ------------------------------
# Work (Many per User)
# ------------------------------
class Work(db.Model):
    __tablename__ = 'Work'
    work_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    language_type = db.Column(db.String(100))
    work_type_id = db.Column(db.Integer, db.ForeignKey('Work_Type.work_type_id'))

# ------------------------------
# Korat Dictionary
# ------------------------------
class KoratWord(db.Model):
    __tablename__ = 'Korat_Language_Dictionary'
    id = db.Column(db.Integer, primary_key=True)
    korat_word = db.Column(db.String(100), unique=True, nullable=False)
    thai_meaning = db.Column(db.String(255), nullable=False)
