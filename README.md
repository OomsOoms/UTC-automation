# UTC-automation
Code to automate UTC competitions with Google sheets and Google forms

## how to use
You need to install some modules using the command 'pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib'

you need to make a google api and give it permission to the spreadsheets it is reading from and writing to
to make a google api follow this video []

input the id of the spreadsheet into the python code and also input the file path to the .json file contaning the keys to access the api

at the moment it reads 100 lines from the preadsheet, this can be changed in the code where is assigns the range
