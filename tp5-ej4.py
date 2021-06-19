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
        
        
        
    return condicion
            
    
def prueba():
    numero = int(input("Ingrese un numero entero positivo: "))
    condicion = numero_perfecto(numero)
    print(f"{numero} es un numero perfecto?: {condicion}")
    
if __name__ == "__main__":
    prueba()
