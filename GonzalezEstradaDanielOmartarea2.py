def verificar_longitud_palabra(palabra):  #Se define la función "Verificar_longitud_palabra" se le pasan el parametro "Palabra"
    longitud = len(palabra)               #La variable "Longitud" con apoyo de la función len ayuda a calcular el número de caracteres
    if 4 <= longitud <= 8:                #Evalua que la variable longitud contenga entre 4 y 8 caracteres
        return "La palabra es correcta."  #Compara y evalua si entra dentro de la condición e imprime el mensaje
    elif longitud < 4:                     #Evalua si el valor de la variable longitud es menor a 4 
        return f"Hacen falta letras. Solo tiene {longitud} letras."  #En el caso de ser menor a 4 evalua el contenido y calcula la cantidad que tiene
    else:                                  #Evalua en el caso de ser mayor a 8 caracteres
        return f"Sobran letras. Tiene {longitud} letras."  #En el caso que la longitud sea mayor devolver la longitud

# Solicitar la entrada del usuario
palabra_usuario = input("Ingresa una palabra: ")      #Entrada del usuario, palabra
resultado = verificar_longitud_palabra(palabra_usuario) 
print(resultado) 
