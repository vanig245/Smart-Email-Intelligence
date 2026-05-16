import json
import requests
# signin
email_name = input("enter your email: ")
if email_name.endswith("@gmail.com"):
    print("hello,", email_name)
    secret_key = input("enter your secret key: ")

    with open("data.json", "r") as file:
        data = json.load(file)        

    # data = {}
    data[email_name] = secret_key

    with open("data.json", "w") as file:
        file.write(json.dumps(data))
    
else:
    print("invalid email.Please write proper email")


login_email = input("enter your login_email: ")

if login_email in data:
    login_secret_key = input("enter your secret key: ")
    if login_secret_key == data[login_email]:
        print("login successful! Hello", login_email)
    else: 
        print("wrong password, please try again")
else: 
    print("wrong email please write again")