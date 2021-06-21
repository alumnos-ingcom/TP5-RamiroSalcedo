################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ""
    
    if texto == texto.upper():
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
    elif texto == texto.lower():
        
        abc = "abcdefghijklmnopqrstuvwxyz0123456789"
        
        
    for letra in texto:
        
        if letra in abc:
           
           texto_cifrado += abc[abc.index(letra)+desplazamiento % (len(abc))]
           
        else:
            
            texto_cifrado += letra


    return texto_cifrado

def decodificado(mensaje, lugares):
    decodificado = ""
    
    if mensaje == mensaje.upper():
        abc = "9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA"
        
    elif mensaje == mensaje.lower():
        
        abc = "9876543210zyxwvutsrqponmlkjihgfedcba"
        
        
    for letra in mensaje:
        
        if letra in abc:
           
           decodificado +=abc[abc.index(letra)+lugares % (len(abc))]
           
        else:
            
            decodificado +=letra


    return decodificado

def prueba():
    texto = input(str("ingrese la cadena que quiere cifrar: "))
    desplazamiento = int(input("ingrese la cantidad de lugares que quiere mover los caracteres: "))
    condificado = cifrado_cesar(texto, desplazamiento)
    mensaje = input(str("ingrese la cadena que quiere descifrar: "))
    lugares = int(input("ingrese la cantidad de lugares que se movieron los caracteres: "))
    decodificador = decodificado(mensaje, lugares)
    print(condificado)
    print(decodificador)
        
if __name__ == "__main__":
    prueba()       