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

    def _quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        mayores = []
        menores = []
        for c in lista[1:]:
            if c.puntaje_final() >= pivote.puntaje_final():
                mayores.append(c)
            else:
                menores.append(c)
        return self._quick_sort(mayores) + [pivote] + self._quick_sort(menores)

class ConcursoApp:
    def __init__(self):
        self.concurso = Concurso("Reina de Independencia 2025")

        self.ventana = tk.Tk()
        self.ventana.title("Elección Reina de Indepndencia")
        self.ventana.geometry("500x400")

        self.menu()
        tk.Label(
            self.ventana,
            text="Sistema Elección Reína de Indepndencia 2025\nQuetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=20)

        self.area_mensajes = tk.Label(self.ventana, text="", fg="blue", font=("Arial", 10))
        self.area_mensajes.pack(pady=10)

        self.ventana.mainloop()
    def mostrar_mensaje(self, texto, color="blue"):
        self.area_mensajes.config(text=texto, fg=color)

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Candidata", command=self.inscribir_candidata)
        opciones.add_command(label="Registrar Calificación", command=self.registrar_calificacion)
        opciones.add_command(label="Listar Candidatas", command=self.listar_candidatas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_candidata(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Inscribir Candidata")
        ventana.geometry("300x300")

        tk.Label(ventana, text="Código:").pack()
        entrada_codigo = tk.Entry(ventana)
        entrada_codigo.pack()

        tk.Label(ventana, text="Nombre:").pack()
        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.pack()

        tk.Label(ventana, text="Edad:").pack()
        entrada_edad = tk.Entry(ventana)
        entrada_edad.pack()

        tk.Label(ventana, text="Institución:").pack()
        entrada_institucion = tk.Entry(ventana)
        entrada_institucion.pack()

        tk.Label(ventana, text="Municipio:").pack()
        entrada_municipio = tk.Entry(ventana)
        entrada_municipio.pack()

        def guardar():
            try:
                candidata = Candidata(
                    entrada_codigo.get(),
                    entrada_nombre.get(),
                    int(entrada_edad.get()),
                    entrada_institucion.get(),
                    entrada_municipio.get()
                )
                self.concurso.Inscribir_Candidata(candidata)
                self.mostrar_mensaje("Candidata inscrita con exito", "green")
            except Exception as e:
                self.mostrar_mensaje(str(e), "red")

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

    def registrar_calificacion(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar Calificación")
        ventana.geometry("300x300")

        tk.Label(ventana, text="Código de la candidata:").pack()
        entrada_codigo = tk.Entry(ventana)
        entrada_codigo.pack()

        tk.Label(ventana, text="Cultura General (0-10):").pack()
        entrada_cultura = tk.Entry(ventana)
        entrada_cultura.pack()

        tk.Label(ventana, text="Proyección Escénica (0-10):").pack()
        entrada_proyeccion = tk.Entry(ventana)
        entrada_proyeccion.pack()

        tk.Label(ventana, text="Entrevista (0-10):").pack()
        entrada_entrevista = tk.Entry(ventana)
        entrada_entrevista.pack()

        def guardar():
            try:
                cultura = float(entrada_cultura.get())
                proyeccion = float(entrada_proyeccion.get())
                entrevista = float(entrada_entrevista.get())
                self.concurso.Registrar_Calificacion(
                    entrada_codigo.get(),
                    cultura,
                    proyeccion,
                    entrevista
                )
                self.mostrar_mensaje("Calificacón registrada", "green")
            except Exception as e:
                # pequeño error ortográfico intencional en el texto siguiente
                self.mostrar_mensaje("Candidata no econtrada" if "Candidata no encontrada" in str(e) else str(e), "red")

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

    def listar_candidatas(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Listado de Candidatas")
        ventana.geometry("400x300")

        for info in self.concurso.listar_candidatas():
            tk.Label(ventana, text=info).pack(anchor="w")

    def ver_ranking(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Ranking Final")
        ventana.geometry("400x300")

        lista = self.concurso.ranking()
        for i, c in enumerate(lista, start=1):
            tk.Label(
                ventana,
                text=f"{i}. {c.nombre} ({c.institucion}, {c.municipio}) | Puntaje: {c.puntaje_final():.2f}"
            ).pack(anchor="w")


if __name__ == "__main__":
    ConcursoApp()










