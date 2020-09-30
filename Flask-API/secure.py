# This is for authentication and identity

#authenticaton
from user import user

users = [
    User(1,'Saravanan','flask@123'),
    User(2,'Vijayamuthu','flask@321')
]

# check JWT docu. for py
username_table = {u.username: u for u in users} #getting username, id (attr. from user.py)
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    #check for user and return 
    user = username_table.get(username,None)
    
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)