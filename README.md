# Application with basic user authorization functionalites.

**Before proceeding with the frontend or api setup, complete the setup of the sql server.**
The project uses MySQL to work. Make sure you have mysql installed in your system and is up.
If you have set password for the root user, provide the credentials accordingly in the api configuration.

###### Steps for backend setup
The backend api has been made with python and flask.
Make sure you have python 3.5+ installed in your system.

In the backend directory, create a virtual environment and install the requirements.
> pip install -r requirements.txt

Perform the migrations.
> python manage.py db init

> python manage.py db migrate

> python manage.py db upgrade

Run the api.
> python manage.py run

*Open the api in browser with localhost:5000 to initialize the database with some values.*

**In order to use your gmail for google login, add your gmail to the user table in the database created after migrating, or create username and password for loggin in normally and run the api again.**

###### Steps for frontend setup
The frontend has been made using Angular.
Make sure your have all the requirements to run an Angular app.

In the frontend directory, run the following command to install the modules required to run the project.
> npm install

Run the application using the following command.
> ng serve

*Open the app in the browser with localhost:4200*

Login to the app using either your gmail or the credentials created.