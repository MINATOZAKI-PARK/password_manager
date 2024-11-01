import secrets as ss
import string as sg

def generate_password(long):
    characters = sg.ascii_letters + sg.digits + sg.punctuation # conjunto de caractertes
    try:
        if long >= 8: # Condicional para que la longitud no sea menor a 8
            while True:
                password = "".join(ss.choice(characters)for _ in range(long)) # Generador de contraseña
                if(any(char in sg.ascii_letters for char in password) and # Verifica si la contraseña tiene al menos un caracter de cada uno
                    any(char in sg.punctuation for char in password) and
                    any(char in sg.digits for char in password)):
                    return password
        else:
            raise ValueError("La longitud mínima recomendada es de 8 caracteres.") # Si se ingresa una longitud menor a 8 lanza este error
        
    except ValueError as e:
        print("Error: ", e)


if __name__ == "__main__": # codigo solo para generator.py
    try:
        length = int(input("Ingrese la longitud de la contraseña: "))
        print("Contraseña generada:", generate_password(length))
    except ValueError as e:
        print("Error:", e)

