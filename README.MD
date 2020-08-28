# Intelimetrica API

Django RestApi that store data about restaurants and their geo positions

# API Deployment URL
**https://intelimetricapi.herokuapp.com/api/v1/restaurants/**

# Documentation Deployment URL
**https://intelimetricapi.herokuapp.com/documentation/**

# Postman Collection
**https://www.getpostman.com/collections/600dfe404a77c4f33edb**


#Modules:
- restaurants
- admin


#Local Requirements:

- Python 3.8
- Django 3.0
- pip requirements are listed in the 'requirements.txt' file in the project


# Local Install instructions:

Before running please follow this steps:

- 1- Create new folder in your selected path(Desktop, Downloads, Documents, etc..)
- 2- Clone this repository and move the unzipped folder to the new folder created previously
- 3- Open your terminal and move it to the path folder created on step 1
- 4- Create a virtual environment using the next command (MacOS):
```
                            python3 -m venv <yourvenvname>
```    

# Running local Intelimetrica API  

- 1- Open your cloned repository (located in your new folder created in previous section) using
     your code editor preferred (PyCharm, VisualStudioCode, ...)
- 2- Open your code editor's terminal and use "cd .." command to move one folder back into directory path
- 3- Activate your virtual environment using the next command(MacOS):
```
                            source <yourvenvname>/bin/activate
```
- 4- Once you have activated your virtual environment, return to your cloned repository (this should be one up folder) using "cd <reponame>" command 
- 5- Install all requirements located in requirements.txt file using the next command:
```
                            pip install -r requirements.txt
```
- 6- Done!!! You can run your local server using the nex command (MacOS):
```
                            python3 manage.py runserver
```
- 7- Open your browser at **127.0.0.1:8000**

#Accessing to Admin Module
 If you want to access to admin module create a superuser following the next steps:
- On your code editor's terminal type the nex command(MacOS) and follow the prompt instructions:
```
                            python3 manage.py createsuperuser
```
Once you have created a superuser go to the next url and access with your superuser credentials
- **http://127.0.0.1:8000/admin/**
Now you can access to admin module's dashboard
NOTE: you can access with follow credentials:
    - username: gonzaloromero
    - password: intelimetrica 

# API endpoints
   - Modules endpoints:
        - **http://127.0.0.1:8000/api/v1/restaurants/** 
        
# Documentation url
- This will be a very useful guide about our API endpoints for its FrontEnd team implementation
                                                - **http://127.0.0.1:8000/documentation/**
        
-NOTE: Unfortunately the statistical data was not implemented because exists an incompatibility between Postgres12 and Postgis
