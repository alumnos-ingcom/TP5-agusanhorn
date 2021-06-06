################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def invertir_mayusculas(texto):
    resultado = ""
    for i in texto:
        if i.isupper():
            i = i.lower()
            resultado += i #Guardarlo en una variable
        elif i.islower():
            i = i.upper()
            resultado += i
        else:
            resultado += i
    return resultado
        
def prueba():
    texto = "a VeR sI sIRVE estA cosa"
    texto = invertir_mayusculas(texto)
    print(texto)    

if __name__ == "__main__":
    prueba()
