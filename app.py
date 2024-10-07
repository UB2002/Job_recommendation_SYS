from flask import Flask
from flask_migrate import Migrate
from database.database import db, JobPosting
from routes import hello, recommendation, posting_job 
import json 
from flask import jsonify
from insert_mock_data import insert_mock_data
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(hello, url_prefix='/')
app.register_blueprint(recommendation, url_prefix='/recommendation') 
app.register_blueprint(posting_job, url_prefix='/jobs')  

with app.app_context():
    db.create_all()
    insert_mock_data()

if __name__ == "__main__":
    app.run(debug=True)
