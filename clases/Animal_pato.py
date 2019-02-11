# Ejemplo de creacion de clases y herencia
# creacion de clase animal y pato

class Animal:
    numero_de_animales = 0

    def __init__(self):
        print('Creando un animal...')
        # atributo de instancia
        self.estoy_vivo = True
        Animal.numero_de_animales += 1

    def crecer(self):
        print('Soy un animal y estoy creciendo')

    def respirar(self):
        print('Soy un animal y estoy respirando')

    def reproducir(self):
        print('Soy un animal y me estoy reproduciendo')

    def morir(self):
        self.estoy_vivo = False
        print('Fui un animal')

    def vivir_o_morir(self):
        self.estoy_vivo = not self.estoy_vivo

class Pato(Animal):
    def __init__(self, nombre_pato='pato',
                 ala_color='blanca',
                 pico_color='cafe'):

        self.ala_color = ala_color
        self.pico_color = pico_color
        self.nombre_pato = nombre_pato
        super().__init__()
        print('Creando un Pato...y me llamo: {}'.format(self.nombre_pato))


    def __str__(self):
        # Para soportar el print de una clase pato
        return 'Soy en pato, me llamo: {} ' \
               'y tengo el ala de color {} y el pico de ' \
               'color {}'.format(self.nombre_pato,
                                 self.ala_color,
                                 self.pico_color)

    def __repr__(self):
        return 'Soy en pato, me llamo: {} ' \
               'y tengo el ala de color {} y el pico de ' \
               'color {}'.format(self.nombre_pato,
                                 self.ala_color,
                                 self.pico_color)

    def __add__(self, other):
        # metodo especial para sumar instancias de tipo pato
        # Pato 1 + Pato2 -> self + other
        return Pato(ala_color=self.ala_color,
                    pico_color=other.pico_color)


#    def respirar(self):
#        print('Hola soy un Pato pero ...')
#        super().respirar()

Donal = Pato('Donal', pico_color='verde', ala_color='negro')
Daisy = Pato('Daisy', pico_color='azul', ala_color='rojo')

print('Sumando 2 patos:', Donal + Daisy)
#print('soy un pato --->', Daisy)

#print('numero de animales:', Animal.numero_de_animales)
#print('Estoy vivo?', animalito.estoy_vivo)
#print('Crezca', animalito.crecer())

#estatus = 'inicial'
#estatus = animalito.respirar()

#if estatus is None:
#    print('que salvada, el animal respiró')
#else:
#    print('Mas noticias a las 6...')