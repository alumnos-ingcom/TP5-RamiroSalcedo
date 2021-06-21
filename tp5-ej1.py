################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def funcion_pares(numero):
    
    
    resultado = numero / 2
    coma = 0.99999
    condicion = resultado + coma
    
    condicion2 = int(resultado) + 1
    
    
    
    if condicion2 < condicion:
        
        return False
    
    elif condicion2 > condicion:

        return True
    
          
    
        
        


def prueba():
    
    numero = int(input("ingrese un valor numerico: "))

    resultado = funcion_pares(numero)

    print(resultado)
    

if __name__ == "__main__":
    prueba()



