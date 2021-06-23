################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def lista(cantidad_numeros):
    
    lst = []
    
    rango = int(cantidad_numeros)

    for i in range(rango):
        
        valor = int(input("Ingrese valor: "))
        
        lst.append(valor)


    return lst

def compararlistas(lista1, lista2):
    
    
    for i in lista1:
        for j in lista2:
            
            if(i==j):
                
                retorno = True
            else:
                
                retorno = False
                
    for i in lista1[::-1]:
        
        for j in lista2:
            if(i==j):
                
                retorno2 = True
            else:
                
                retorno2 = False
        
    if (retorno2 == True) or (retorno == True):
        resultado = True
    else:
        resultado = False
    
                
    return resultado


def prueba():
    cantidad_numeros1 = input("ingrese cuantos numeros quiere tener su lista: ")
    lista1 = lista(cantidad_numeros1)
    lista2 = lista(cantidad_numeros1)
    evalua = compararlistas(lista1, lista2)
    print(evalua)
    
    
if __name__ == "__main__":
    prueba()    