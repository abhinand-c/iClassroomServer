# iClassroom ![logo](https://github.com/mastercharizardx/iClassroomServer/blob/master/app/static/favicon.svg)
For Demo visit : https://iclassroom.herokuapp.com/ and use the following credentials:  
Username: demo
Password: demo


## [iClassroom-Video RTC Server](https://github.com/mastercharizardx/iClassroom-Video)
Please refer https://github.com/mastercharizardx/iClassroom-Video for the WebRTC based node.js server used for the virtual class and video conferencing services of iClassroom


## Local Installaion

Create a python environment (Refer: [Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or [Python venv](https://docs.python.org/3/tutorial/venv.html) )
Install dependencies listed in requirements.txt ` pip instal -r requirements.txt `

### Create a superuser
Before running the server for the first time, create a superuser account
` python manage.py createsuperuser ` 

### Run the Server Locally
` python manage.py runserver `


## Deployment in Heroku
 Refer https://devcenter.heroku.com/articles/deploying-python
 