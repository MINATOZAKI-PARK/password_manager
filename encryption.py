from cryptography.fernet import Fernet 
from generator import generate_password

def claveGL():
    key = Fernet.generate_key()
    with open("clave.key", "wb") as key_file:
        key_file.write(key)

    with open("clave.key", "rb") as key_file:
        return key_file.read()




keyC = claveGL()
fernet = Fernet(keyC)
password = generate_password(12)


def cifrado(pword):
    pword.encode()
    password = fernet.encrypt(pword)
    print(f'Contrasena cifrada...')
    return password


passwordCifrada = cifrado()
contrasenaDesifrada = fernet.decrypt(passwordCifrada)
print(f'Contrasena descifrada: {contrasenaDesifrada.decode()}')








