################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Calcular factoriales
#40585 = 24 + 1 + 120 + 40320 + 120 = 4! + 0! + 5! + 8! + 5! 


def calcular_factorial(lista):
    lista_factoriales = []
    for i in lista:
        factorial = 1
        if i == "0":
            lista_factoriales.append(factorial)
        else:
            for i in range(1, int(i)+1):
                factorial *= i #"*=" multiplica a la variable del lado izquierdo el valor del lado derecho
            lista_factoriales.append(factorial)
    return lista_factoriales
        
def calcular_factoriones():
    factoriones = []
    for j in range(0,1499999):
        suma = 0
        factoriales0 = []
        for i in str(j):
            factoriales0.append(i)
        factoriales = calcular_factorial(factoriales0)
        for i in factoriales:
            suma += i
        if j == suma:
            factoriones.append(j)  
    return factoriones
    
def prueba():
    resultado = calcular_factoriones()
    print(resultado)
    
if __name__ == "__main__":
    prueba()

