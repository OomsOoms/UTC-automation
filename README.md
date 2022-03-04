# UTC-automation
Code to automate UTC competitions with Google sheets and Google forms

## how to use
You need to install some modules using the command ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

You need to make a google api and give it permission to the spreadsheets by using the share option on the top right of the spreadsheets you are using.

To make a google api follow this video [Google Sheets - Python API, Read & Write Data by Learn Google Spreadsheets](https://youtu.be/4ssigWmExak)
download the key as a .json file and name it 'keys.json'

Put 'keys.json' in the folder 'UTC automation'
when running the code, input the ur of the spreadsheet you want to read from into the python code first,
the second url you enter is the spreadsheet where it will write to
