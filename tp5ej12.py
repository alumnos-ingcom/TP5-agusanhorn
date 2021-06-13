################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def comparacion_de_listas(lista1, lista2):
    if len(lista1) == len(lista2):
        try:
            for i in lista1:
                lista2.index(i)       
            return True
        except:
            return False
    else:
        return False
    
def prueba():
    lista1 = ["a", 1, 3, 36, "b", "c"]
    lista2 = ["a", "b", "c", 1, 3, 36]
    resultado = comparacion_de_listas(lista1, lista2)
    if resultado:
        print(f"{resultado}: las listas no contienen los mismos elementos")
    else:
        print(f"{resultado}: las listas contienen los mismos elementos entre si")

if __name__ == "__main__":
    prueba()


