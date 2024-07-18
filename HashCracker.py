import hashlib

hash_file = "096fb77cbef0fa3ea16407106fd037be99748e25fc4d97422d127f121c9d60ce"

dic_file = input("Ingrese la direccion del archivo del diccionario: ")

with open(dic_file, 'r') as file:
    diccionario = [line.strip() for line in file]
    for password in diccionario:
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()
        if hash_calculado == hash_file:
            print(f"La contraseña original es: {password}")
            break
        else:
            print("La contraseña no se encuentra en el diccionario.")
