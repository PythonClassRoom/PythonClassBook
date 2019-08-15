# lambda funcion para aplanar la lista de listas
flatten = lambda l: [item for sublist in l for item in sublist]

def returnNotMatches(a, b):
    a = set(a)
    b = set(b)
    return [list(b - a), list(a - b)]

def intersection(a, b):
    a = set(a)
    b = set(b)
    return list(b & a)

class Clinica(dict):
    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_paciente(self,identificación,
                        Nombre, Apellido,
                        teléfono, dirección,
                        lista_de_enfermedades_tratadas,
                        lista_de_medicamentos_que_toma):
        self.update({
            identificación :{
            'Nombre':Nombre,
            'Apellido':Apellido,
            'teléfono':teléfono,
            'dirección':dirección,
            'lista_de_enfermedades_tratadas':lista_de_enfermedades_tratadas,
            'lista_de_medicamentos_que_toma':lista_de_medicamentos_que_toma}
        })

        print('Paciente agregado',repr(self[identificación]))

    def borrar_paciente(self, identificacion):
        print('Borrando Paciente', repr(self[identificacion]))
        if identificacion in self:
            del self[identificacion]

    def agregar_medicinas(self,identificacion, nuevo_medicamento):
        self[identificacion]['lista_de_medicamentos_que_toma'].append(nuevo_medicamento)

    def agregar_enfermedades(self,identificacion, nueva_enfermedad):
        self[identificacion]['lista_de_enfermedades_tratadas'].append(nueva_enfermedad)

    def enfermedades_tratadas(self):
        return flatten([self[paciente_id]['lista_de_enfermedades_tratadas'] for paciente_id in self.keys()])

    def medicamentos_recetados(self):
        return flatten([self[paciente_id]['lista_de_medicamentos_que_toma'] for paciente_id in self.keys()])

    def comparar_pacientes(self, paciente1_id, paciente2_id):
        #Creando funcion reporte. notese que el formato es similar
        def reporte(Mensaje, funcion_a_ejecutar, detalle):
            print(Mensaje,
                  'Paciente:' ,paciente1_id,
                  'Paciente:', paciente2_id,
                  funcion_a_ejecutar(
                      self[paciente1_id][detalle],
                      self[paciente2_id][detalle])
                  )
        reporte('Medicamentos en común', intersection, 'lista_de_medicamentos_que_toma')
        reporte('Medicamentos diferentes', returnNotMatches, 'lista_de_medicamentos_que_toma')
        reporte('Enfermedades en común', intersection, 'lista_de_enfermedades_tratadas')
        reporte('Enfermedades diferentes', returnNotMatches, 'lista_de_enfermedades_tratadas')

#Instancia clinica, creando una clinica
la_clinica = Clinica('Hospital Central')

#Definiendo pacientes
juanito = {'identificación':1,'Nombre':'Juan','Apellido':'Mora','teléfono':24578451,
'dirección':'San Jose 3 st, 5 Av','lista_de_enfermedades_tratadas' : ['dolor de cabeza'],
'lista_de_medicamentos_que_toma': ['aspirina', 'panadol']}

carlitos = {'identificación':2,'Nombre':'Carlos','Apellido':'Fernandez','teléfono':47845465,
'dirección':'Heredia 1 st, 3 Av','lista_de_enfermedades_tratadas' : ['dolor de espalda'],
'lista_de_medicamentos_que_toma': ['voltaren', 'panadol']}

anita = {'identificación':3,'Nombre':'Ana','Apellido':'Picado','teléfono':4857848,
'dirección':'Cartago 5 st, 9 Av','lista_de_enfermedades_tratadas' : ['Fibroma', 'dolor de cabeza'],
'lista_de_medicamentos_que_toma': ['voltaren', 'panadol']}

#Agregando pacientes
la_clinica.agregar_paciente(**juanito)
la_clinica.agregar_paciente(**carlitos)
la_clinica.agregar_paciente(**anita)

# agregando más información
la_clinica.agregar_medicinas(identificacion=1,nuevo_medicamento='acetaminofen')
la_clinica.agregar_enfermedades(identificacion=1,nueva_enfermedad='fiebre')

#Creando reportes
reporte_enfermedades_tratadas = la_clinica.enfermedades_tratadas()
reporte_medicamentos_recetados = la_clinica.medicamentos_recetados()

#Comparando pacientes
la_clinica.comparar_pacientes(1,3)

#Borrando Pacientes
la_clinica.borrar_paciente(2)
