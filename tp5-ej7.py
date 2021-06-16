################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def calculardistancia(numero1, numero2):
    
    distancia = 0
    
    if numero1 > numero2:
        
        while numero1 > numero2:
            
            distancia = distancia + 1
            numero2 = numero2 + 1
            
    elif numero2 > numero1:
        
        while numero2 > numero1:
            
            distancia = distancia + 1
            numero1 = numero1 + 1
            
    else:
        distancia = 0
            
    return distancia

def prueba():
    
    numero1 = int(input("ingrese punto numerico a para medir distancia: "))
    numero2 = int(input("ingrese punto numerico b para medir distancia: "))
    
    distancia = calculardistancia(numero1, numero2)
    print(f"la distancia entre los dos numeros es de: {distancia}")
 
if __name__ == "__main__":
    prueba()
        