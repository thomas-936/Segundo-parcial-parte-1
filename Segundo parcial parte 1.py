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





