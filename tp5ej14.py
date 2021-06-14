################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def definir_si_es_capicua(numero):
    if numero <= 9:
        return True
    else:
        numero = str(numero)
        return numero == numero[::-1]


def prueba():
    numero = 101
    resultado = definir_si_es_capicua(numero)
    if resultado:
        print(f"El numero {numero} si es capicúa")
    else:
        print(f"El numero {numero} no es capicua")

if __name__ == "__main__":
    prueba()


