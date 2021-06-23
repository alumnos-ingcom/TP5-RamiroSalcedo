################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def lista(cantidad_numeros):
    
    lst = []
    
    rango = int(cantidad_numeros)

    for i in range(rango):
        
        (valor) = int(input("Ingrese valor: "))
        
        lst.append(valor)


    return lst

def promedio_movil(longitud, lista):
    contador = 0 
    valor = 0
    promedio = []
    cantidad = len(lista)
    a = 0    
  
        
    for i in range(0, (cantidad-1)):
    
        a += 1
        valor = lista[i] + lista[i+1]

        promedio.append(valor/longitud)
        
        
    return promedio
    
    
def prueba():
    cantidad_numeros = input("ingrese la cantidad de valores que va a promediar: ")
    numeros = lista(cantidad_numeros)
    longitud = int(input("ingrese cada cuanto quiere tomar el promedio: "))
    promedio = promedio_movil(longitud, numeros)
    print(f"Los promedios moviles son: {promedio}")
 
if __name__ == "__main__":
    prueba()
    