# Job Recommendation System

This repository contains the Job Recommendation System project. The following instructions will help you set up the project on your local machine.

## Requirements

- Python 3.x
- Flask
- Flask-Migrate
- Any other dependencies in `requirements.txt`

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/UB2002/Job_recommendation_SYS.git
cd Job_recommendation_SYS
```

### 2. Set up a Virtual Environment
Create a virtual environment to isolate the project dependencies:
```bash
# On Linux or macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Requirements
After activating the virtual environment, install the necessary dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 4. Set Up Flask Environment Variables
Set the required environment variables to run Flask. You can either do this in the terminal or create a .env file.

```bash 
set FLASK_APP=app.py
```

### 5. Initialize the Database
This project uses Flask-Migrate for handling database migrations. Run the following commands to initialize the database and apply migrations.

1.Initialize the Flask-Migrate setup:
  This creates a migrations directory and prepares the app for migrations:

  ```bash
  flask db init
  ```
2.Create a Migration:
This command generates a new migration based on the changes to your models (if any):

```bash
flask db migrate -m "Initial migration"
```
3.Apply the Migration:
This command applies the migration to your database (creating tables, adding columns, etc.):

```bash
flask db upgrade
```


### 6. Running the Application
After setting up the database, you can run the Flask application:
```bash
flask run
```
