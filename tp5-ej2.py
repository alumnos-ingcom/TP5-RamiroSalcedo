################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def fibonacci(numero):
    
    variable1 = 0
    variable2 = 1
    
    if numero > 2:
        
        for i in range(numero):
            
            resultado = variable1 + variable2
            
            variable1 = variable2
            
            variable2 = resultado
            
            numero = numero + 1
            
    return resultado




def prueba():
    numero = int(input("Ingrese el n-esimo numero de la serie de fibonacci que quiere saber: "))
    variable = fibonacci(numero)
    print(f"El {numero} numero de la serie de fibonacci es {variable}")
    


if __name__ == "__main__":
    prueba()
            
