################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def funcion_pares(numero):
    
    
    if numero % 2 == 0:
        
        variable = True
        
    else:
        
        variable = False
        
        
    return variable
        
        


def prueba():
    
    funcion_pares(2)

    resultado = funcion_pares(3)

    print(resultado)
    pass

if __name__ == "__main__":
    prueba()



