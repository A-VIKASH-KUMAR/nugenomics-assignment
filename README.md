# nugenomics-assignment
## To run the app use the following commands for backend
 - Create virtual environmenet 
    $ python3 -m venv .venv
 - Activate the terminal 
    $ source .venv/bin/activate
 - Install the dependencies from requirements.txt
    $ pip install -r requirements.txt (from backend folder)
 - Run fast api app from backend folder
    $ fastapi dev app.py
 - Server starts to run on http://127.0.0.1:8000 as base url
 1) call /auth/register endpoint to create a user
 2) call /auth/login endpoint to login a user and generate the access token
 3) call /auth/reset-password to reset a existing password if forgot 

# Command to start frontend
- $ python -m http.server 8080
- Redirect to http://0.0.0.0:8080/ to open the ui