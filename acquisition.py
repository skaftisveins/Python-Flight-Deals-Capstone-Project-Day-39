from config import *
import requests


class Acquisition:
    def __init__(self, first_name, last_name, user_email, verify_email) -> None:
        self.first_name = first_name,
        self.last_name = last_name,
        self.user_email = user_email,
        self.verfiy_email = verify_email
        
    def get_user_input(self):
        print("Welcome to Skafti's Flight Club.")
        print("We find the best flight deals and email you the details.")
        self.first_name = input("What is your first name?")
        self.last_name = input("What is your last name?")
        self.user_email = input("What is your email?")
        self.verify_email = input("Type your email again.")

        if self.user_email == self.verify_email:
            return True
        else:
            None
            
        new_member = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.user_email
            }
        }
        response = requests.post(
            sheety_users_endpoint, headers=sheety_headers, json=new_member)
        print(response.text)
