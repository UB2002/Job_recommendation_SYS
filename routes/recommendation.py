from flask import Blueprint, request, jsonify
from database.database import db, JobPosting
from sqlalchemy import or_
recommendation = Blueprint("recommendation", __name__)

    # Example data structure you might receive
    # data = {
    #     "skills": ["Python", "Machine Learning"],
    #     "location": "Remote",
    #     "job_type": "Full-Time"
    # }
@recommendation.route("/", methods=["POST"])
def recommend_jobs():
    data = request.get_json()
    
    skills = data.get("skills", [])
    location = data.get("location", "")
    job_type = data.get("job_type", "")

    query = JobPosting.query

    if skills:
        query = query.filter(or_(*[JobPosting.required_skills.contains(skill) for skill in skills]))

    if location:
        query = query.filter(JobPosting.location == location)

    if job_type:
        query = query.filter(JobPosting.job_type == job_type)

    recommended_jobs = query.all()

    job_list = []
    for job in recommended_jobs:
        job_list.append({
            "id": job.id,
            "job_title": job.job_title,
            "company": job.company,
            "required_skills": job.required_skills,
            "location": job.location,
            "job_type": job.job_type,
            "experience_level": job.experience_level
        })

    return jsonify({"recommended_jobs": job_list}), 200

# from flask import Blueprint, request, jsonify
# recommendation = Blueprint("recommendation", __name__)

# @recommendation.route("/", methods=["GET"])
# def recommend():
#     return "recommned jobs route working"