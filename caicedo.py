print('Caicedo')

class Caicedo:
    def __init__(self, nombre, apellido, migajero=True):
        self.nombre = nombre
        self.apellido = apellido
        self.migajero = migajero

    def migajear(self, persona):
            return f'Estoy migajeando a.... {persona}'

    def __str__(self):
        return f'{self.nombre} {self.apellido} es migajero: {self.migajero}'


caicedo = Caicedo('Jonnathan', 'Caiza')
print(caicedo.migajear('Abbi'))
print(caicedo)