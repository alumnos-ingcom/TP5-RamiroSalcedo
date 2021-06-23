################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def buscar_palabra(texto, palabra):
    
    lugar = 0
    palabras = texto.split(' ')
    
    for i, j in enumerate(palabras):
            
            
        if palabra == j:
                
            lugar = i + 1
                
                     
                    
            
    return lugar

def prueba():
    texto = input("ingrese texto: ")
    palabra = input("Que palabra desea buscar?: ")
    linea = buscar_palabra(texto, palabra)
    print(f"La palabra se encuentra en la posicion: {linea}")
    
    
if __name__ == "__main__":
    prueba()                