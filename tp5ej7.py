################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancia(num1, num2):
    if num1 >= num2:
        result = num1 - num2
    else:
        result = -num1 + num2
    return result

def prueba():
    num1 = 4
    num2 = -3
    num = distancia(num1, num2)
    print(num)

if __name__ == "__main__":
    prueba()
