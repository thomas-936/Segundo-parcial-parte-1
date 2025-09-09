"""
Segundo parcial
"""
import tkinter as tk

class Candidata:
    def __init__(self, codigo, nombre, edad, institucion, municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.institucion = institucion
        self.municipio = municipio
        self.calificaciones = []

    def Agrega_Calificacion(self, cultura, proyeccion, entrevista):
        promedio =(cultura + proyeccion + entrevista ) / 3
        self.calificaciones.append(promedio)

    def Puntaje_Final(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def Mostrar_Info(self):
        return f"{self.codigo} - {self.nombre} ({self.institucion}, {self.municipio}) | Puntaje: {self.Puntaje_Final(): .2f}"

class Concurso:
    def __init__(self , nombre):
        self.nombre = nombre
        self.candidatas = []

    def Inscribir_Candidata (self, candidata):
        for c in self.candidatas:
            if not c.codigo == candidata.codigo:
                raise ValueError("Ya existe una candidata inscrita con este codigo. \n Intente de Nuevo")
            self.candidatas.append(candidata)


    def Registrar_Calificacion(self, codigo, cultura, proyeccion, entrevista):
        for c in self.candidatas:
            if c.codigo == codigo:
                c.agregar_calificacion(cultura, proyeccion, entrevista)
                return
        raise ValueError("Candidata no encontrada \n Intente de Nuevo")

    def listar_candidatas(self):
        return  [c.mostrar_info() for c in self.candidatas]

    def ranking(self):
        lista = self.candidatas[:]
        return self._quick_sort(lista)








