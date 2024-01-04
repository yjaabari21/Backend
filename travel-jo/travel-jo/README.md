# Travel Jo
To run the apis locally you need to run the below command line
```
uvicorn main:app --reload
```

APIs Deployed server 
* https://mysterious-everglades-33537-6877cf5cef3c.herokuapp.com/docs

## Topics

### Python Fast API 
* https://fastapi.tiangolo.com/

### JSON format

* https://www.flickr.com/services/api/response.json.html#:~:text=JSON%2C%20or%20JavaScript%20Object%20Notation,from%20other%20languages%20too!)

### Pyrebase4
* https://github.com/nhorvath/Pyrebase4

### Firebase 
* https://firebase.google.com/docs/reference/rest/database

### How to deploy your APIs on Heroku server

Deploying your FastAPI application to a free server involves a few steps. Here's a general guide to deploying a FastAPI application on a server using a service like Heroku:

1. Prepare Your FastAPI Application
Make sure your FastAPI application is well-organized and contains all the necessary files. You should have a main.py file (or a file with your FastAPI application) and any required dependencies specified in a requirements.txt file.

2. Create a Procfile
Create a Procfile in the root of your project. This file is used by Heroku to determine how to run your application. For a basic FastAPI application, the Procfile can be as simple as:

plaintext
Copy code
```
web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
```

Replace main with the name of your file (without the .py extension) if it's different.

3. Set Up a runtime.txt (Optional)
Create a runtime.txt file if you want to specify a particular version of Python. For example:
```
python-3.9.*
```

4. Create a requirements.txt File
Ensure you have a requirements.txt file that lists all the dependencies of your FastAPI application. You can generate this file using the following command:
```
pip freeze > requirements.txt
```

5. Create a Heroku Account
If you don't have a Heroku account, sign up for a free account at Heroku.

6. Install Heroku CLI
Install the Heroku Command Line Interface (CLI) by following the instructions on the Heroku CLI page.

* https://devcenter.heroku.com/articles/heroku-cli

```
brew tap heroku/brew && brew install heroku
```

7. Log in to Heroku
Open a terminal and log in to your Heroku account using the following command:

```
heroku login
```

8. Create a New Heroku App
Create a new Heroku app using the following command:
```
heroku create
```

9. Deploy Your App
Deploy your FastAPI application to Heroku using Git:
```
git add .
git commit -m "Initial commit"
git push heroku master

```
10. Open Your App in the Browser
Once the deployment is successful, open your app in the browser using: