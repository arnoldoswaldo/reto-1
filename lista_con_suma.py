# función que recibe una lista de números y retorna la suma de los dos mayores números de la lista.
# se divide en 2 partes para obtener los dos mayores números y luego sumarlos.
# Autor: [Arnold Acosta].

def numeros_mayores(numeros):

    a = max(numeros)
    numeros.remove(a)
    b = max(numeros)
    return [a, b]

def lista_con_suma(numeros):
    mayores = numeros_mayores(numeros)
    suma = sum(mayores)
    return suma

# Define la cantidad de numeros a validar para crear una lista
numeros = []
cantidad = int(input("Cuantos números desea sumar: "))

# almacena los numeros en la lista
for _ in range(cantidad):
  num = int(input("Ingrese un número: "))
  numeros.append(num)

# Imprime la suma de los dos mayores números
print("La suma de los dos mayores números es:", lista_con_suma(numeros))


def main():
    if __name__ == "__main__":
        main()
