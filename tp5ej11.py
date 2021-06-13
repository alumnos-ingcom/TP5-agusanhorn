################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def promedio_movil(lista, promediar):
    largo = len(lista)
    desde = 0
    resultado = [lista[0]]
    promediar1 = promediar
    while largo > 1:
        suma = []
        for i in lista[desde:promediar]:
            suma.append(i)
            suma_de_valores = 0
            if len(suma) == promediar1:
                for z in suma:
                    suma_de_valores += z
                resultado.append(suma_de_valores / promediar1)
        desde += 1
        promediar += 1
        largo -= 1
    return resultado


def prueba():
    lista = [23, 43, 54, 65]
    promediar = 2
    resultado = promedio_movil(lista, promediar)
    print(f"El promedio movil de {lista} promediado en {promediar} es: {resultado}")

if __name__ == "__main__":
    prueba()

