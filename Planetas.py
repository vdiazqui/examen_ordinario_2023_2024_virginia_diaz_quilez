
class ClaseEstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000

    def destruir_planeta(self, planeta):
        if planeta.clasificacion <= self.puntos_de_vida:
            self.puntos_de_vida -= planeta.clasificacion
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
        else:
            print(f"La Estrella de la Muerte no puede destruir el planeta {planeta.nombre} debido a su alta clasificación.")
            
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

def main():
    # Creación de instancias de cada uno de los planetas
    concordia = Concordia()
    ilum = Ilum()
    kamino = Kamino()
    
    # Crear una instancia de la Estrella de la Muerte
    estrella = ClaseEstrellaDeLaMuerte()

    # Para cada planeta, intentar destruirlo con la Estrella de la Muerte
    for planeta in [concordia, ilum, kamino]:
        estrella.destruir_planeta(planeta)
        print(f"{planeta.nombre} - Volumen: {planeta.volumen} km³, Clasificación: {planeta.clasificacion}")
# Verifica si este script es el punto de entrada principal
if __name__ == '__main__':
    main()