# Creacion de la clase base llamada Planeta
class Planeta:
    #Constructor de la clase Planeta
    def __init__(self,nombre,volumen,clasificacion):
        # Inicialización de los atributos de la clase
        self.nombre= nombre # Nombre del planeta
        self.volumen= volumen # Volumen del planeta en kilómetros cúbicos
        self.clasificacion= clasificacion # Clasificación numérica del planeta

# Creación de la subclase Concordia, que hereda de Planeta
class Concordia(Planeta):
    # Constructor de la subclase Concordia
    def __init__(self):
        # Llamada al constructor de la clase madre con los atributos específicos de Concordia
        super().__init__("Concordia", 500, 1)

# Creación de la subclase Ilum, que también hereda de Planeta
class Ilum(Planeta):
    # Constructor de la subclase Ilum
    def __init__(self):
        # Llamada al constructor de la clase madre con los atributos específicos de Ilum
        super().__init__("Ilum", 1200, 2)
# Creación de la subclase Kamino, que hereda de Planeta
class Kamino(Planeta):
    # Constructor de la subclase Kamino
    def __init__(self):
         # Llamada al constructor de la clase padre con los atributos específicos de Kamino
        super().__init__("Kamino", 800, 3)

# Definición de la función principal del script
def main():
    # Creación de instancias de cada uno de los planetas
    concordia = Concordia()
    ilum = Ilum()
    kamino = Kamino()
    
    # Para cada planeta, mostramos su información
    for planeta in [concordia, ilum, kamino]:
        # Imprime el nombre, volumen y clasificación de cada planeta
        print(f"{planeta.nombre} - Volumen: {planeta.volumen} km³, Clasificación: {planeta.clasificacion}")

# Verifica si este script es el punto de entrada principal
if __name__ == '__main__':
    # Si es así, ejecuta la función main()
    main()