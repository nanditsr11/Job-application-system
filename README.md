# Job Application System
A Django-based job portal that allows users to view job listings and apply by uploading resumes in PDF or Word format. The portal also provides an admin interface to manage and upload job listings, as well as define screening questions.
________________________________________
## Features

### User Side:
- View job listings with detailed descriptions.
- Apply for jobs by uploading resumes (PDF or Word format).
- Answer screening questions (Yes/No or numerical format).
- View job details such as job title, location, job description, and job ID.

### Admin Side:
- Admins can upload and manage job listings.
- Admins can add screening questions to the job listings.
- Admins can monitor job applications and user responses.
________________________________________

## Project Setup

Follow the steps below to get the project up and running on your local machine.

### Prerequisites
- Python 3.6+
- Django 3.x+
- (Optional) Virtual Environment (recommended)

### Installation
1.	Clone the repository:
-	git clone https://github.com/yourusername/job-application-system.git 
-	cd job-application-system
2.	Create a Virtual Environment (Optional but recommended):
-	python -m venv venv
3.	Activate the Virtual Environment:
o	Windows:
- venv\Scripts\activate
o	Linux/Mac:
source venv/bin/activate
4.	Install dependencies: Make sure you have all necessary dependencies installed by running:
-	pip install -r requirements.txt

If you don't have a requirements.txt file, install Django manually:
-	pip install django

## Set Up Database
- Run migrations to set up the database:
- python manage.py migrate

## Create a Superuser
- To access the Django admin panel, you'll need to create a superuser:
- python manage.py createsuperuser
- You’ll be prompted to enter a username, email, and password.
________________________________________

## Running the Project
1.	Start the Django Development Server:
-	Run the following command to start the Django server:
-	python manage.py runserver 
2.	Access the Application: Open your web browser and go to:
-	http://127.0.0.1:8000  

The application should be live, and you can start interacting with it.
________________________________________

## Accessing the Admin Panel

To manage job listings, log in to the Django admin panel:

1.	Open a browser and go to:
-	http://127.0.0.1:8000/admin  
2.	Log in with the superuser credentials you created earlier.
3.	From there, you can add new jobs, upload resumes, and manage screening questions.
________________________________________________________________________________

## Dependencies
The project requires the following Python packages:

- Django
- django-crispy-forms (for better form rendering)
- django-fileupload (for file upload functionality)
- python-docx (for handling Word files)
- PyPDF2 (for handling PDF files)

You can install all required packages using:
- pip install -r requirements.txt
________________________________________

## Future Improvements
- Add job search functionality.
- Integrate with email services to send application confirmations.
- Implement user authentication (login and registration for users).
- Add job categories and filtering options.
- Allow admins to review and approve job applications.
________________________________________
## License
This project is licensed under the MIT License - see the LICENSE file for details.
________________________________________
## Contributions
Feel free to fork the project and submit pull requests with new features or bug fixes! 

