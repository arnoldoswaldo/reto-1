# Descripcion: Este programa verifica si una palabra o frase es un palíndromo.
# Autor: [Arnold Acosta]   
def palindromo(text):
    # para liminar los espacios en blanco y convertir el texto a minúsculas
    text = text.replace(" ", "").lower()

    # Crear una lista con las letras del texto en orden inverso
    text_list = list(text)
    text_list.reverse()

    # Comparar el texto original con la lista invertida
    if text == "".join(text_list):
        return True
    else:
        return False

# Solicita información al usuario
text = input("Ingrese una palabra o frase: ")

# Llama a la funcion  y muestra el resultado
if palindromo(text):
    print("el texto",text, "es un palíndromo.")
else:
    print("el texto",text, "no es un palíndromo.")
def main():
    if __name__ == "__main__":
    main()