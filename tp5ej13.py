################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    pass

def busqueda_de_palabra(texto, palabra):
    texto = texto.lower()
    palabra = palabra.lower()
    lista = []
    palabras_lista = ""
    for i in texto:
        if i == " ":
            lista.append(palabras_lista)
            palabras_lista = ""
        else:
            palabras_lista += i
    if palabras_lista:
        lista.append(palabras_lista)
    try:
        posicion = lista.index(palabra)
        return posicion
    except ValueError as err:
        raise IngresoIncorrecto(f"La palabra '{palabra}' no se encuentra en el texto") from err
    
def prueba():
    texto = "Welcome to Jurassic Park"
    palabra = "par"
    resultado = busqueda_de_palabra(texto, palabra)
    print(f"La posición de {palabra} en el texto es {resultado}")
    
if __name__ == "__main__":
    prueba()

