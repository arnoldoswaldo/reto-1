# Descripcion: Este programa realiza operaciones matematicas basicas
# Autor: [Arnold Acosta]      

def operaciones():
    while True:
        num1= int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))
        operacion = input("ingrese la operacion que desea realizar(+,-,/,*): ")  
        if operacion == "+":
            resultado= (num1 + num2)
            print("el resultado es: ", resultado)
        elif operacion == "-":
            resultado= (num1 - num2)
            print("el resultado es: ", resultado)
        elif operacion == "*":
            resultado= (num1 * num2)
            print("el resultado es: ", resultado)
        elif operacion == "/":
            resultado= (num1 / num2)
            print("el resultado es: ", resultado)
                
        else:  
            print("operacion invalida")
    
        otra_operacion = input("¿Desea realizar otra operación? (s/n): ")
        if  otra_operacion.lower() == "n":
            
         break
           
        else:
            return operaciones ()                    

operaciones()
def main():
    if __name__ == "__main__":
         main()

