################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def numero_perfecto(num):
    suma = 0
    for i in range(1, num):
        divisor = num % i
        if divisor == 0:
            suma += i #Guardarlo en una variable
    if suma == num:
        return True
    else:
        return False

def prueba():
    num = 6 #Número a verificar
    num = numero_perfecto(num)
    if num == True:
        print(f"El número es perfecto ---> {num}")
    else:
        print(f"El número no es perfecto ---> {num}")

if __name__ == "__main__":
    prueba()


