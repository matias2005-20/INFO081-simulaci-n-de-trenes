import tkinter as tk
from PIL import Image, ImageTk
from config import titulo, alto, ancho

from datos import rutas_guardadas, estaciones_guardadas, trenes_guardados
from ui.eliminar import eliminar_tren, eliminar_ruta, eliminar_estacion
from ui.crear import crear_estacion, crear_ruta, crear_tren

import json #forma de guardar datos


ventanafaz = None  #ventanafaz para todo global


def guardar_datos():
    datos = {
        "rutas": rutas_guardadas,
        "estaciones": estaciones_guardadas,
        "trenes": trenes_guardados
    } #datos en diccionarios por el json 

    with open("datos_guardados.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)  
    print("Datos guardados correctamente.")


def cargar_datos():
    try:
        with open("datos_guardados.json", "r", encoding="utf-8") as f:
            datos = json.load(f)

        # guardar los datos y lipia datos
        rutas_guardadas.clear()
        rutas_guardadas.extend(datos.get("rutas", []))

        estaciones_guardadas.clear()
        estaciones_guardadas.extend(datos.get("estaciones", []))

        trenes_guardados.clear()
        trenes_guardados.extend(datos.get("trenes", []))

        print("Datos cargados correctamente.")
        print("Rutas:", rutas_guardadas)
        print("Estaciones:", estaciones_guardadas)
        print("Trenes:", trenes_guardados)

    except FileNotFoundError:
        print("No hay archivo para cargar (datos_guardados.json).")


def eliminar_elemento():
    
    ventana_eliminar = tk.Toplevel(ventanafaz)
    # al toplevel le cambie la variable a ventanafaz para que esa sea la principal y no tener una ventana suelta por ahi
    ventana_eliminar.title("Eliminar elemento")
    ventana_eliminar.geometry("300x200")

    tk.Button(ventana_eliminar, text="Eliminar tren",
              command=lambda: eliminar_tren(ventanafaz)).pack(pady=10)
    tk.Button(ventana_eliminar, text="Eliminar ruta",
              command=lambda: eliminar_ruta(ventanafaz)).pack(pady=10)
    tk.Button(ventana_eliminar, text="Eliminar estación",
              command=lambda: eliminar_estacion(ventanafaz)).pack(pady=10)


def emergencia():
    print("Evento climático, tener cuidado.")


def abrir_menu(ventanain):
    """Ventana principal del menú."""
    global ventanafaz
    ventanain.destroy()

    ventanafaz = tk.Tk() 
    ventanafaz.title(titulo)
    ventanafaz.geometry(f"{ancho}x{alto}")

    try:
        imagen = Image.open("mmmmmmm.png")
        imagen_tk = ImageTk.PhotoImage(imagen)
        fondo = tk.Label(ventanafaz, image=imagen_tk)
        fondo.image = imagen_tk
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception:
        print("No se pudo cargar la imagen 'mmmmmmm.png'.")

    tk.Button(ventanafaz, text="Crear", command=ventana_crear_opciones).place(x=20, y=20)
    tk.Button(ventanafaz, text="Guardar", command=guardar_datos).place(x=20, y=60)
    tk.Button(ventanafaz, text="Cargar", command=cargar_datos).place(x=20, y=100)
    tk.Button(ventanafaz, text="Eliminar", command=eliminar_elemento).place(x=20, y=140)
    tk.Button(ventanafaz, text="Cerrar", command=ventanafaz.destroy).place(x=20, y=180)

    tk.Button(ventanafaz, text="EMERGENCIA", fg="red", command=emergencia).place(x=20, y=220)

    ventanafaz.mainloop()


def ventana_crear_opciones():
    ventana_op = tk.Toplevel(ventanafaz)
    ventana_op.title("Crear")
    ventana_op.geometry("250x200")

    tk.Button(ventana_op, text="Crear tren", command=lambda: crear_tren(ventanafaz)).pack(pady=10)
    tk.Button(ventana_op, text="Crear estación", command=lambda: crear_estacion(ventanafaz)).pack(pady=10)
    tk.Button(ventana_op, text="Crear ruta", command=lambda: crear_ruta(ventanafaz)).pack(pady=10)
