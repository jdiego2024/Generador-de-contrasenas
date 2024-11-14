import random
import time

print("           Generador de Contraseñas               ")
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")


while True:

    def generar_contraseñas(largo_contraseña):
        caracteres = "+-/*!#$%&()=¿?'¡¨´[],;.:abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        contraseña = ""

        for _ in range(largo_contraseña):
            contraseña += random.choice(caracteres)  # Añade un carácter aleatorio a la contraseña

        return contraseña

    # Solicitar al usuario la longitud de la contraseña y convertirla a un entero
    largo = int(input("¿Qué tan larga quieres tu contraseña? "))

    print("Generando...")
    time.sleep(1.5)
    print("Tu contraseña es:", generar_contraseñas(largo))
