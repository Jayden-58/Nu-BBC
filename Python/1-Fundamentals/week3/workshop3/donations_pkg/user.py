def login(database, username, password):
    if username in database.keys() and password in database[username]: #maybe need to change 
        print("welcome: " + username)
        return username
    else:
        print("Failure")
        return ""

def register(database, username):
    if len(username) >= 10:
        print("username is too long, must be less than 10 characters")
        return ""
    if username.lower() in database.keys():
        print("username already registered...")
        return ""
    else:
        print("username: " + username + " is now registered")
        return username
        
