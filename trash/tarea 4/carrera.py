import math
import random

class vehiculo:
    limite = 1000
    numero_ciclos = 0
    def __init__(self, nombre):
        self.avance = 0
        self.estatus = False
        self.fuerza = 0
        self.nombre = nombre

    def __repr__(self):
        return self.nombre

    def generar_fuerza(self):
        return random.uniform(0, 9)

    def check_limite(self):
        self.estatus =  vehiculo.limite < self.avance
        return self.estatus

    def avanzar(self, funcion_rendimiento):
        if not self.check_limite():
            self.fuerza = self.generar_fuerza()
            self.avance +=  math.ceil(funcion_rendimiento(self.fuerza))
            vehiculo.numero_ciclos += 1
        return self.check_limite()

class bus(vehiculo):
    def __init__(self):
        super(bus, self).__init__(nombre='bus')

    def avanzar(self):
        return super(bus, self).avanzar(funcion_rendimiento=lambda x: 5*x)


class tractor(vehiculo):
    def __init__(self):
        super(tractor, self).__init__(nombre='tractor')

    def avanzar(self):
        return super(tractor, self).avanzar(funcion_rendimiento=math.log2)

class camion(vehiculo):
    def __init__(self):
        super(camion, self).__init__(nombre='camion')

    def avanzar(self):
        return super(camion, self).avanzar(funcion_rendimiento=lambda x: 2 * x + 1)

class sedan(vehiculo):
    def __init__(self):
        super(sedan, self).__init__(nombre='sedan')

    def avanzar(self):
        return super(sedan, self).avanzar(funcion_rendimiento=lambda x: 3 * x**2)


mi_bus = bus()
mi_tractor = tractor()
mi_sedan = sedan()
mi_camion = camion()

lista_vehiculos = [mi_bus, mi_tractor, mi_sedan, mi_camion]

while not any([i.avanzar() for i in lista_vehiculos]):
    print([(i.nombre, i.avance) for i in lista_vehiculos])

print('Ganador:', [(i.nombre, i.avance) for i in lista_vehiculos if i.estatus] )
print('Los vehículos hicieron:' , vehiculo.numero_ciclos, 'ciclos')

pass