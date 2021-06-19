################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def tribonacci(numero):
    
    variable1 = 0
    variable2 = 1
    variable3 = 1
    
    if numero > 3:
        
        for i in range(numero):
            
            resultado = variable1 + variable2 + variable3
            
            variable1 = variable2
            
            variable2 = variable3
            
            variable3 = resultado
            
            
            
            
    return resultado




def prueba():
    numero = int(input("Ingrese el n-esimo numero de la serie de tribonacci que quiere saber: "))
    variable = tribonacci(numero)
    print(f"El {numero} numero de la serie de tribonacci es {variable}")
    


if __name__ == "__main__":
    prueba()
            