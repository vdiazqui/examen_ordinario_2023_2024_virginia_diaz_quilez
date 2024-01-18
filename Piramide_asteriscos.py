#Definimos la función pirámide
def piramide(n):
        # Verificar que n es mayor o igual a 1
        if n < 1:
            return "El número debe ser mayor o igual a 1."
        # Generar la pirámide de asteriscos
        for i in range(n):
            # Calcular la cantidad de asteriscos para el nivel actual
            asteriscos = "*" * (2 * i + 1)
            # Centrar los asteriscos y añadirlos a la pirámide
            print(asteriscos.center(2 * n - 1))

def main():
    # Solicitar al usuario que ingrese un número entero
    n = int(input("Introduzca un numero entero de niveles para la piramide (mayor o igual a 1): "))
    while n<1:
        n = int(input("Por favor, introduzca un numero mayor o igual a 1: "))
    else:
        piramide(n)

if __name__ == '__main__':
   main()