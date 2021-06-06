################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def tribonacci(num):
    termino0 = 1
    termino1 = 1
    termino2 = 1
    for i in range(num):
        sumadeterminos = termino0 + termino1 + termino2
        termino0 = termino1
        termino1 = termino2
        termino2 = sumadeterminos
    return termino1
    
def prueba():
    num = 8 #Que el bucle se repita 8 veces
    num = tribonacci(num)
    print(f"El n-esimo termino de tribonacci es: {num}")
    
if __name__ == "__main__":
    prueba()


