# ITI-Crowd-Funding-App

### This is a Python-based application that allows users to create and donate to crowdfunding campaigns.
-------------------------------------------

### Installation
1- Clone the repository
2- Create and activate a virtual environment using virtualenv or conda
3- Install the required dependencies using pip:
```
pip install -r requirements.txt
```
Set up the database by running the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
Create a superuser account by running:
```
python manage.py createsuperuser
```
Start the development server:
```
python manage.py runserver
```
Open your web browser and navigate to http://localhost:8000/ to view the application.
Usage
User Authentication
Users can sign up for an account or log in using their existing credentials. After logging in, users can create crowdfunding campaigns, donate to existing campaigns, and track their donation history.

### Creating a Campaign
To create a campaign, the user must fill out a form that includes the campaign's name, description, funding goal, and end date. Upon successful submission, the campaign is added to the list of active campaigns.

### Donating to a Campaign
Users can donate to an existing campaign by selecting it from the list of active campaigns and entering a donation amount. If the donation is successful, the user's name and donation amount are added to the campaign's list of contributors.

### Contributions
Contributions to this project are welcome. To contribute:

Fork the repository
Create a new branch for your changes
Make your changes and commit them with descriptive commit messages
Push your changes to your fork
Submit a pull request
