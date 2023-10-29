import os
import pandas as pd
from manim import *

def cargarData(archivo):
    if not os.path.exists(archivo):
        print(f"No se control {archivo}")
        return None
    data = pd.read_csv(archivo)
    return data

class miembros(Scene):
    def construct(self):
        miembros_bruto = cargarData("miembros.csv")
        
        # Obtener la opción del usuario
        opcion = input("Ingrese 'N' para ordenar por Nivel o 'T' para ordenar por Tiempo: ").upper()

        # Ordenar el DataFrame según la opción elegida por el usuario
        if opcion == "N":
            miembros_temp = miembros_bruto.sort_values(by="Tiempo total como miembro (meses)", ascending=False)
            miembros = miembros_temp.sort_values(by="Nivel actual", ascending=True)
        elif opcion == "T":
            miembros = miembros_bruto.sort_values(by="Tiempo total como miembro (meses)", ascending=False)
        else:
            print("Opción inválida. No se realizará ningún ordenamiento.")
            miembros = miembros_bruto

        #miembros = cargarData("miembros.csv")
        if miembros is None:
            return

        # Crear un rectángulo para el fondo
        fondo = Rectangle(
            width=config["frame_width"],
            height=config["frame_height"],
            fill_color="#000000",
            fill_opacity=0.65,
            stroke_width=0,
            z_index=-1  # Para que esté detrás de otros objetos
        )

        # Agregar el rectángulo al fondo de la escena
        self.add(fondo)

        txGracias = Text("Gracias por su apoyo", slant=ITALIC).scale(1.5)
        txGracias.shift(2.5 * UP)

        self.play(Write(txGracias))

        for nombres in miembros["Miembro"]:
            print(nombres)
            imagen = ImageMobject(f"fotos_miembros/{nombres}.jpg").scale(0.2)
            self.add(imagen)

            nombreMiembro = Text(nombres).scale(1.2)
            nombreMiembro.move_to([0,-1.5,0])

            border = nombreMiembro.copy()
            border.set_stroke(color=BLUE, width=8)
            self.add(border, nombreMiembro)
            self.play(
                       FadeIn(nombreMiembro, shift=DOWN, Scale=0.66), 
                       FadeIn(imagen, shift=DOWN, Scale=0.66),
                       FadeIn(border, shift=DOWN, Scale=0.66),)
            
            self.play(FadeOut(nombreMiembro, shift=DOWN * 2, Scale=1.5), FadeOut(imagen, shift=DOWN * 2, Scale=1.5),FadeOut(border, shift=DOWN * 2, Scale=1.5))
            #return
        self.wait(2)
