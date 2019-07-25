# Nicola Blackstock
#Assignment 3 Part 2
#Due Date: June 19th 2019
# UCBE Cyber Security 

# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below
def getCreds():
    username = input('Enter Username ')
    password = input('Enter Password ')

    userInfo = {
        'username': username,
        'password': password
        } 
    return(userInfo)

def checkLogin(userInfo, adminList):

    user_input = (userInfo['username'])
    input_pwd = (userInfo['password'])
    user1 = (adminList[0]['username'])
    pwd1 = (adminList[0]['password'])
    user2 = (adminList[1]['username'])
    pwd2 = (adminList[1]['password'])

    if(user_input == user1 and input_pwd == pwd1) or (user_input == user2 and input_pwd == pwd2) :
        loggedIn = True
        print("YOU HAVE LOGGED IN!")  
    else:
        loggedIn = False
        print("LOGIN FAILED")
        print('----------------')
    while loggedIn == False:
        get_user_info = getCreds()
        checkLogin(get_user_info, adminList)
        break
    

get_user_info = getCreds()
checkLogin(get_user_info, adminList)
