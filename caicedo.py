print('Caicedo')

print("adhdjbajdads")


class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def migajiar(self, nombre):
        return f'{nombre} dame migajas'

caiza = Persona('caiza', 19, 'Ecuador')
print(caiza.migajiar("abbii"))
