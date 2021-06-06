################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def parentesis_balanceado(corchetes):
    resultado = []
    corchetesvalido = {"[": "]"}
    for i in corchetes:
        if i in corchetesvalido:
            resultado += i
        elif len(resultado) == 0 or i != corchetesvalido[resultado.pop()]:
            return False
    return len(resultado) == 0
        

def prueba():
    corchetes = "[[[[][]]]]"
    parentesis = parentesis_balanceado(corchetes)
    if parentesis == True:
        print("Perfectamente equilibrado, como todo debe estar")
    else:
        print("Los corchetes no están balanceados")
    

    
if __name__ == "__main__":
    prueba()