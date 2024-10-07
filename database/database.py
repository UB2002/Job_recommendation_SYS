from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.JSON, nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)
    preferences = db.Column(db.JSON, nullable=False)

class JobPosting(db.Model):
    __tablename__ = 'job_postings'

    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    required_skills = db.Column(db.JSON, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)
    