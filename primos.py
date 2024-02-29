# Descripcion: Programa que crea una lista e  imprime los números primos  dados por el usuario
# Autor: [Arnold Acosta]   
def es_primo(num): 
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Define la cantidad de numeros a validar para crear una lista
numeros = []
cantidad = int(input("Cuantos números desea validar: "))

# almacena los numeros en la lista
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

# Imprime si los números son primos
for num in numeros:
    if es_primo(num):
        print(num, "es numero primo")
    else:
        print(num, "no es numero primo")
def main(): 
    if __name__ == "__main__":
        main()



