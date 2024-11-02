from cryptography.fernet import Fernet

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