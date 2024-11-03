from cryptography.fernet import Fernet

def generateKey(clave= "clave.key"): # Parametro predefinido para no ingresa un nombre
    key = Fernet.generate_key()  # genera la key 

    with open(clave , "wb") as key_file: # Crea un archivo para escribir la key 
        key_file.write(key) # Eacribe la Key en el archivo

    print(f"Clave generada y guardada en {clave}")



def loadKey(clave= "clave.key"):
    try:
        
        with open(clave, "rb") as key_file: # abre el arcivo
            key = key_file.read() # lee el archivo 
        return key # lo retorna 
    
    except FileNotFoundError: # lanza esto si no encuentra el archivo
        print(f"Error: No se pudo encontrar el archivo {clave}.") 
        return None # Retorna None