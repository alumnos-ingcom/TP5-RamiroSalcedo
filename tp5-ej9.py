################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def factoriales(numero):

    if numero == 0:
        factorial = 1
    else:
        factorial = numero * factoriales(numero - 1)
        
    return factorial
    

def factoriones():
    factoriones = 1, 2, 148, 40585, 2540160
    digito = []
    numero = []
    resultado = 0
    lista = []
    
    for i in range(145):
        
        numero = i
        
        for a in range(len(str(numero))):
            str(numero)
            entero = numero[a]
            factorial = factoriales(entero)
            
            resultado = resultado + factorial
            
            if resultado == i:
            
                lista.append(i)

    return lista
            
            
            
    
        
def prueba():
    imprime = factoriones()
    print(imprime)
    
if __name__ == "__main__":
    prueba()       