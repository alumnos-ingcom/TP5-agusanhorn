################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificacion(texto, posicion):
    cifrado = ""
    letras = "abcdefghijklmnñopqrstuvwxyz"
    for i in range(len(texto)): #Longitud del texto y posición de las letras a números
        letra = texto[i] #Se extrae la letra desde la primer posición
        if (letra.islower()): #Verifica si es minuscula
            unicode = chr((ord(letra) + posicion - 97) % 26 + 97)
            #Convierte la letra en códigounicode
            #Suma la posición dada y resta 97(a), modulo 26 para asegurarse de que esté en el abecedario(1, 26) + 97 que da el número en unicode
            #al final se pasa de número a caracter
            cifrado += unicode
        elif letra == " ":
            cifrado += " " #Para agregar los espacios
        else:
            return "No es un texto en minúsculas"
    return cifrado

def decodificacion(texto2, posicion2):
    descifrado = ""
    letras = "abcdefghijklmnñopqrstuvwxyz"
    for i in range(len(texto2)):
        letra = texto2[i]
        if (letra.islower()):
            unicode = chr((ord(letra) - 97 - posicion2) % 26 + 97)
            descifrado += unicode
        elif letra == " ":
            descifrado += " "
        else:
            return "No es un texto en minúsculas"
    return descifrado

def prueba():
    texto = "el cifrado del cesar"
    posicion = 13
    resultado = codificacion(texto, posicion)
    print(resultado)
    texto2 = "ry pvsenqb qry prfne"
    posicion2 = 13
    resultado2 = decodificacion(texto2, posicion2)
    print(resultado2)

if __name__ == "__main__":
    prueba()
