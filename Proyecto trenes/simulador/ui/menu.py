import tkinter as tk
from PIL import Image, ImageTk
from config import titulo, alto, ancho, color

def eliminar_elemento():
    """Ventana para eliminar tren, ruta o estación."""
    ventana_eliminar = tk.Toplevel(ventanafaz) 
    #al toplevel le cambie la variable a ventanafaz para que esa sea la principal y no tener una ventana suelta por ahi
    ventana_eliminar.title("Eliminar elemento")
    ventana_eliminar.geometry("400x200")

    tk.Button(ventana_eliminar, text="Eliminar tren").place(x=30, y=30)
    tk.Button(ventana_eliminar, text="Eliminar ruta").place(x=150, y=30)
    tk.Button(ventana_eliminar, text="Eliminar estación").place(x=270, y=30)

def crear_tren():
    """Ventana para crear tren."""
    ventana_tren = tk.Toplevel(ventanafaz) #lo mismo lo cambie a ventana faz
    ventana_tren.title("Crear tren")
    ventana_tren.geometry("400x400")

    tk.Label(ventana_tren, text="Nombre del tren:").pack(pady=5)
    nombre_text = tk.Text(ventana_tren, height=2, width=40)
    nombre_text.pack(pady=5)

    tk.Label(ventana_tren, text="Rutas:").pack(pady=5)
    rutas_text = tk.Text(ventana_tren, height=2, width=40)
    rutas_text.pack(pady=5)

    tk.Label(ventana_tren, text="Estaciones:").pack(pady=5)
    estaciones_text = tk.Text(ventana_tren, height=2, width=40)
    estaciones_text.pack(pady=5)

    def mostrar_texto():
        print("Nombre:", nombre_text.get("1.0", "end-1c"))
        print("Rutas:", rutas_text.get("1.0", "end-1c"))
        print("Estaciones:", estaciones_text.get("1.0", "end-1c"))

    tk.Button(ventana_tren, text="Mostrar datos", command=mostrar_texto).pack(pady=10)

def abrir_menu(ventanain):
    """Ventana principal del menú."""
    global ventanafaz #tuve que hacerla gobal para poder usarla en las funciones de arriba
    ventanain.destroy() #esto es para que una vez que iniciemos se cierra la ventana que sobraba en mi opinion
    ventanafaz = tk.Tk() #a qui dejo a ventanafaz como principal
    ventanafaz.title(titulo) #init
    ventanafaz.geometry(f"{ancho}x{alto}")#importado de init

    try:
        imagen = Image.open("mmmmmmm.png")
        imagen_tk = ImageTk.PhotoImage(imagen)
        fondo = tk.Label(ventanafaz, image=imagen_tk)
        fondo.image = imagen_tk
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception:
        print("No se pudo cargar la imagen 'mmmmmmm.png'.")

    # Botones del menú
    tk.Button(ventanafaz, text="Crear", command=crear_tren).place(x=20, y=20)
    tk.Button(ventanafaz, text="Guardar").place(x=20, y=60)
    tk.Button(ventanafaz, text="Cargar").place(x=20, y=100)
    tk.Button(ventanafaz, text="Eliminar", command=eliminar_elemento).place(x=20, y=140)
    tk.Button(ventanafaz, text="Cerrar", command=ventanafaz.destroy).place(x=20, y=180)

    ventanafaz.mainloop()