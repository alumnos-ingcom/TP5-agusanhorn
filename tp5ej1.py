################
# Agustin Anhron - @agusanhorn
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def par_o_impar(num):
    while num > 0:
        num = num - 2
    if num == 0:
        return True #par
    else:
        return False #impar

def prueba():
    num = 537 #Numero a verificar si es par o impar
    num = par_o_impar(num)
    if num == False:
        print("El número es impar")
    else:
        print("El número es par")
    
if __name__ == "__main__":
    prueba()  


