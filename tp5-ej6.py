################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def balancear_parentesis(cadena):
    abre = ["[","{","("]
    cierra = ["]","}",")"]
    almacena = []
    
    for i in cadena:
        
        if i in abre:
            
            almacena.append(i)
            
        elif i in cierra:
            
            a = cierra.index(i)
            
            if ((len(almacena) > 0) and (abre[a] == almacena[len(almacena)-1])):
                almacena.pop()
                
            else:
                return 'NO'
            
    if len(almacena) == 0:
        
        return 'OK'


def prueba():
    cadena = input("ingres su cadena de parentesis: ")
    resultado = balancear_parentesis(cadena)
    print(resultado)
    
            
if __name__ == "__main__":
    prueba()                   
