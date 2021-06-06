################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def fibonacci(num):
    termino0 = 0
    termino1 = 1
    for i in range(num):
        sumadeterminos = termino0 + termino1
        termino0 = termino1
        termino1 = sumadeterminos
    return termino1
    
def prueba():
    num = 8 #Que el bucle se repita 8 veces
    num = fibonacci(num)
    print(f"El n-esimo termino de fibonacci es: {num}")
    
if __name__ == "__main__":
    prueba()
