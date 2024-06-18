'''
Backend Servers Using Python :
# FLask,Django,FastAPI

Communication Protocols:
# TCP/IP
# FTP
# SFTP
# SMTP
# HTTPS ,etc

HTTP Requests methods :
# Post - Create (eg : Creating a Posts in Social media,the data is get entried from your computer to the server)
# Get  - Read() (eg : Reading the replys, comments from that post ,is done from your computer to the server)
# Put  - Update (eg : changes making in the post,from your computer to the server )
# Delete - Remove (eg : deleting the post , from your computer to the server)

Sending a Requests to server:
# Using urls based on the server address called IP

Response :
 Response  denotes the status from the server based on the requests
   # info                - 100+
   # success             - 200+
   # redirection         - 300+
   # cleint error        - 400+ 
   # server error        - 500+

   # 999+ User Defined Status code

eg : 404 Error (Internet / url incorrection (User End))

'''

from flask import Flask
from requests import request # Sending Requests and Getting Response

app = Flask(__name__) # Creating __name__ object for Flask class and storing int the variable app


@app.route('/') # routing the app web (http://127.0.0.1:5000/) ,we can customize this creating new pages (http://127.0.0.1:5000/login )

def Home():
   return "Hello"

'''Note : When you return any value That should be in String , 
if any other type fo type casting because to display the result in the UI'''

if __name__ == '__main__':
    app.run(debug=True) # Running the server in the  local host
