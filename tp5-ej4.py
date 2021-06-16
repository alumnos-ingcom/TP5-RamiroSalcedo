################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def numero_perfecto(numero):
    
    suma = 0
    
    for i in range(1, numero):
        
        if numero % i == 0:
            
            suma = suma + i
    
    
    condicion = suma == numero
        
        
    if condicion == True:
        
        print(f"{numero} es un numero perfecto")
        
        
    else:
        
        print(f"{numero} no es un numero perfecto")
        condicion = False
        
    return condicion
            
    
def prueba():
    numero = int(input("Ingrese un numero entero positivo: "))
    numero_perfecto(numero)
    
    
if __name__ == "__main__":
    prueba()
