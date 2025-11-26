import tkinter as tk
from datos import rutas_guardadas, estaciones_guardadas, trenes_guardados


def crear_estacion(ventanafaz):  
    ventana_estacion = tk.Toplevel(ventanafaz)
    ventana_estacion.title("Crear estación")
    ventana_estacion.geometry("300x200")

    tk.Label(ventana_estacion, text="Nombre de la estación:").pack(pady=5)
    texto = tk.Text(ventana_estacion, height=2, width=30)
    texto.pack(pady=5)

    def guardar_estacion():
        nombre = texto.get("1.0", "end-1c")
        if nombre.strip():  #para eliminar de nombres molestos como ejemplo "    s    " y que solo sean "s"
            estaciones_guardadas.append(nombre.strip())
            print("Estaciones guardadas:", estaciones_guardadas)
        ventana_estacion.destroy()

    tk.Button(ventana_estacion, text="Guardar estación", command=guardar_estacion).pack(pady=10)



def crear_ruta(ventanafaz):  
    ventana_ruta = tk.Toplevel(ventanafaz)
    ventana_ruta.title("Crear ruta")
    ventana_ruta.geometry("300x200")

    tk.Label(ventana_ruta, text="Nombre de la ruta:").pack(pady=5)
    texto = tk.Text(ventana_ruta, height=2, width=30)
    texto.pack(pady=5)

    def guardar_ruta():
        nombre = texto.get("1.0", "end-1c")
        if nombre.strip():
            rutas_guardadas.append(nombre.strip())
            print("Rutas guardadas:", rutas_guardadas)
        ventana_ruta.destroy()

    tk.Button(ventana_ruta, text="Guardar ruta", command=guardar_ruta).pack(pady=10)



def crear_tren(ventanafaz):
    """Ventana para crear tren."""
    ventana_tren = tk.Toplevel(ventanafaz)
    ventana_tren.title("Crear tren")
    ventana_tren.geometry("400x500")

    tk.Label(ventana_tren, text="Crear tren").pack(pady=5)

    tk.Label(ventana_tren, text="Nombre del tren:").pack(pady=5)
    nombre_text = tk.Text(ventana_tren, height=2, width=40)
    nombre_text.pack(pady=5)

    #guarda rutass 
    tk.Label(ventana_tren, text="Ruta:").pack(pady=5)

    if rutas_guardadas:
        ruta_puntito = tk.StringVar(ventana_tren)
        for r in rutas_guardadas:
            tk.Radiobutton(ventana_tren, text=r, variable=ruta_puntito, value=r).pack(anchor="w")
    else:
        tk.Label(ventana_tren, text="No existe ruta").pack(pady=5)
        ruta_puntito = None

    # guardar estacion
    tk.Label(ventana_tren, text="Estación:").pack(pady=5)

    if estaciones_guardadas:
        estacion_puntito = tk.StringVar(ventana_tren) #puntito marcado
        for e in estaciones_guardadas:
            tk.Radiobutton(ventana_tren, text=e, variable=estacion_puntito, value=e).pack(anchor="w")
    else:
        tk.Label(ventana_tren, text="No existe estación").pack(pady=5)
        estacion_puntito = None

    def mostrar_texto():
        nombre = nombre_text.get("1.0", "end-1c")
        print("Nombre:", nombre)

        ruta_sel = ruta_puntito.get() if ruta_puntito else None
        estacion_sel = estacion_puntito.get() if estacion_puntito else None

        if ruta_sel:
            print("Ruta:", ruta_sel)
        if estacion_sel:
            print("Estación:", estacion_sel)

        #guardar tren
        if nombre.strip():
            tren = {
                "nombre": nombre.strip(),
                "ruta": ruta_sel,
                "estacion": estacion_sel
            }
            trenes_guardados.append(tren)  
            print("Trenes:", trenes_guardados)  

        ventana_tren.destroy()

    tk.Button(ventana_tren, text="Mostrar datos", command=mostrar_texto).pack(pady=10)