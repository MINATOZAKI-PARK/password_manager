import secrets as ss
import string as sg

def generate_password(long):
    characters = sg.ascii_letters + sg.digits + sg.punctuation
    while True:
        password = "".join(ss.choice(characters)for _ in range(long))
        if(any(char in sg.ascii_letters for char in password) and 
           any(char in sg.punctuation for char in password) and
           any(char in sg.digits for char in password)):
            return password
