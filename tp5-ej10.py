################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def entero_a_binario(numero):
    
    numero_parametro = int(numero)
    #asigno a binario cada valor de caracter pasado a formato byte con 'b'
    #metiendo un for dentro para que se ejecute en cada numero de letra y no
    #solo en el primer numero
    binario = format(numero_parametro, 'b')
        
    return binario

def binario_a_texto(cadena):
    numero = 0
    
 
    numero = int(cadena, 2)
    
    return numero


def prueba():
    numero = input("ingrese su numero para convertir a binario: ")
    binario = entero_a_binario(numero)
    cadena = input("ingrese su cadena binaria para convertir a numero: ")
    texto = binario_a_texto(cadena)
    
    print(f"su numero en binario es: {binario}")
    print(f"su cadena binaria a numero es: {texto}")
    
    
if __name__ == "__main__":
    prueba()