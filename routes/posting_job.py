from flask import Blueprint, request, jsonify
from database.database import db, JobPosting
import json
posting_job = Blueprint("posting_job", __name__)

@posting_job.route("/", methods=["POST"])
def post_job():
    data = request.get_json()

    required_fields = ['job_title', 'company', 'required_skills', 'location', 'job_type', 'experience_level']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    new_job = JobPosting(
        job_title=data['job_title'],
        company=data['company'],
        required_skills=data['required_skills'],
        location=data['location'],
        job_type=data['job_type'],
        experience_level=data['experience_level']
    )
    
    db.session.add(new_job)
    db.session.commit()

    return jsonify({"message": "Job posted!" , "id": new_job.id, "job_title": new_job.job_title, "company": new_job.company, "required_skills": new_job.required_skills,
    'location': new_job.location, 'job_type': new_job.job_type, 'experience_level': new_job.experience_level }), 201

@posting_job.route("/", methods=["GET"])

def get_jobs():
    jobs = JobPosting.query.all()
    jobs_list = [{
        "id": job.id,
        "job_title": job.job_title,
        "company": job.company,
        "required_skills": job.required_skills,
        "location": job.location,
        "job_type": job.job_type,
        "experience_level": job.experience_level
    } for job in jobs]

    return jsonify(jobs_list), 200

@posting_job.route("/delete_all", methods=["DELETE"])
def delete_all_jobs():
    # Delete all job postings
    num_rows_deleted = JobPosting.query.delete()
    db.session.commit()

    return jsonify({"message": f"{num_rows_deleted} job postings deleted successfully."}), 200


'''
test for if this route is working or not

from flask import Blueprint, request, jsonify
posting_job = Blueprint("posting_job", __name__)


@posting_job.route("/", methods=["GET"])
def post_job():
    return "post job route working"
'''
