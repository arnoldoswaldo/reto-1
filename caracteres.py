# descripción: Programa que recibe palabras y valida cuales tienen los mismos caracteres
# Autor: [Arnold Acosta]
def encontrar_iguales(lista_palabras):
   #diccionario que almacena las palabras
    iguales = {}

    for palabra in lista_palabras:
        # ordena los caracteres de la palabra
        letras = ''.join(sorted(palabra))

        # repetidos
        if letras in iguales:
            iguales[letras].append(palabra)
        else:
            # si no existe
            iguales[letras] = [palabra]

    # validacion
    lista_iguales = [palabras for palabras in iguales.values() if len(palabras) > 1]

    return lista_iguales

lista_palabras = []
while True:
    palabra = input("Ingrese una palabra a la vez, al escribir  0,se validara cuales palabras tienen las mismas letras: ")
    if palabra== "0":
        break
    lista_palabras.append(palabra)

lista_iguales = encontrar_iguales(lista_palabras)

print("Elementos con los mismos caracteres:", lista_iguales)
def main():
    if __name__ == "__main__":
         main()
