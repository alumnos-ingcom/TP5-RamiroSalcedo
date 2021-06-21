################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def cambiar_letras(texto):
    
    
    frase = texto
    cadena = []
    
    for i in range(0, len(frase)):
        
        if (frase[i] != ' '): 
            if (frase[i] >= 'a' and frase[i] <='z'):

                cadena.append(frase[i].upper())

            elif (frase[i] >= 'A' and frase[i] <= 'Z'):

                cadena.append(frase[i].lower())
                
        else:
                
            cadena.append(frase[i])
                     
    
    inversion = "".join(cadena)
    return inversion


def prueba():
    
    texto = input("ingrese su frase/palabra que quiera cambiar: ")
    
    frase = cambiar_letras(texto)
    
    print(frase)
    
    
if __name__ == "__main__":
    prueba()

    