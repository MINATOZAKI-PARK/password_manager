from cryptography.fernet import Fernet 

# prueba
# from generator import generate_password
# from keyManager import generateKey, loadKey

# pasado a keyManager
"""
def generateKey(clave= "clave.key"):
    key = Fernet.generate_key()
    with open(clave , "wb") as key_file:
        key_file.write(key)
    print(f"Clave generada y guardada en {clave}")

def loadKey(clave= "clave.key"):
    try:
        with open(clave, "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {clave}.")
        return None
"""

def encryptPassword(password, key): # Resive contraseña y key
    try:
        fernet = Fernet(key) 
        passwordEncrypt = fernet.encrypt(password.encode()) # encripta la contraseña y la pasa a bit
        print(f'Contrasena cifrada...')
        return passwordEncrypt
    
    except Exception as e:
        print(f"Error al cifrar: {e}")
        return None


def decryptPassword(password, key):
        try:
            fernet = Fernet(key)
            passwordDecrypt = fernet.decrypt(password).decode() # Desencripta la contraseña
            print(f'Contrasena descifrada')
            return passwordDecrypt

        except Exception as e:
            print(f"Error al cifrar: {e}")
            return None



if __name__ == "__main__":



    encrypt = encryptPassword(None)

    decrypt = decryptPassword(None)







