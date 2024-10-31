import secrets as ss
import string as sg

def generate_password(long):
    characters = sg.ascii_letters + sg.digits + sg.punctuation
    if long >= 8:
        while True:
            password = "".join(ss.choice(characters)for _ in range(long))
            if(any(char in sg.ascii_letters for char in password) and 
                any(char in sg.punctuation for char in password) and
                any(char in sg.digits for char in password)):
                return password
    else:
        raise ValueError("La longitud mínima recomendada es de 8 caracteres.")



if __name__ == "__main__":
    try:
        length = int(input("Ingrese la longitud de la contraseña: "))
        print("Contraseña generada:", generate_password(length))
    except ValueError as e:
        print("Error:", e)

