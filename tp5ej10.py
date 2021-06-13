################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def numero_a_texto_binario(numero):
    lista_residuos = []
    while numero >= 1:
        lista_residuos.append(numero % 2)
        numero = int(numero / 2)
    digitos = lista_residuos[::-1]
    return digitos

def texto_binario_a_texto(binario):
    binario = int(binario)
    suma = 0
    posicion = 0
    while binario >= 1:
        digitos = binario % 10
        binario = int(binario/10)
        suma = suma + digitos * (2**posicion)
        posicion = posicion + 1
    return suma

def prueba():
    numero = 135
    resultado1 = numero_a_texto_binario(numero)
    print(f"La representación binaria de {numero} es :{resultado1}")
    binario = "1101"
    resultado2 = texto_binario_a_texto(binario)
    print(f"El codigo binario {binario} representado en número entero es: {resultado2}")
    
if __name__ == "__main__":
    prueba()

