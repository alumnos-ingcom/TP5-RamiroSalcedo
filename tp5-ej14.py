################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def numero_capicua(numero):
    
    if numero > 0:
        #converti el numero en una cadena para evaluarlo a la inversa
        cadena = str(numero)
        
        #evaluo la cadena y retorno true en caso de capicua
        #false en caso de no ser capicua
        if cadena == cadena[::-1]:
            
            retorno = True
            
        else:
            
            retorno = False
            
    return retorno


def prueba():
    numero = int(input("ingrese un numero para ver si es capicua: "))
    retorno = numero_capicua(numero)
    print(retorno)
    
if __name__ == "__main__":
    prueba()
            