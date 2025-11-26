import tkinter as tk
from datos import rutas_guardadas, estaciones_guardadas, trenes_guardados


def eliminar_ruta(ventanafaz):
    ventana = tk.Toplevel(ventanafaz)  
    ventana.title("Eliminar ruta")  
    ventana.geometry("300x300")  

    tk.Label(ventana, text="Eliminar ruta").pack(pady=5)  
    if not rutas_guardadas: 
        tk.Label(ventana, text="No existe ruta").pack(pady=10)  #mensaje en caso de que no hay
        return  

    ruta_puntito = tk.StringVar(ventana)  #StringVar es nesesaria para los puntitos, para seleccionar boton
    

    for r in rutas_guardadas:  
        tk.Radiobutton(ventana, text=r, variable=ruta_puntito, value=r).pack(anchor="w")  

    def confirmar():  
        rutas_guardadas.remove(ruta_puntito.get())  #elimina la ruta
        print("Rutas actuales", rutas_guardadas)  
        ventana.destroy()  

    tk.Button(ventana, text="Eliminar", command=confirmar).pack(pady=10)  


def eliminar_estacion(ventanafaz):  
    ventana = tk.Toplevel(ventanafaz)  
    ventana.title("Eliminar estación")  
    ventana.geometry("300x300")  

    tk.Label(ventana, text="Eliminar estación").pack(pady=5)  

    if not estaciones_guardadas:  
        tk.Label(ventana, text="No existe estación").pack(pady=10)  
        return  

    estacion_puntito = tk.StringVar(ventana)  
    

    for e in estaciones_guardadas: 
        tk.Radiobutton(ventana, text=e, variable=estacion_puntito, value=e).pack(anchor="w")  

    def confirmar():  
        estaciones_guardadas.remove(estacion_puntito.get())  
        print("Estaciones ahora:", estaciones_guardadas)  
        ventana.destroy()  

    tk.Button(ventana, text="Eliminar", command=confirmar).pack(pady=10)  


def eliminar_tren(ventanafaz):  
    ventana = tk.Toplevel(ventanafaz)  
    ventana.title("Eliminar tren")  
    ventana.geometry("300x300")  

    tk.Label(ventana, text="Eliminar tren").pack(pady=5)  

    if not trenes_guardados:  
        tk.Label(ventana, text="No existe tren").pack(pady=10)  
        return  

    tren_puntito = tk.StringVar(ventana)  
    

    # mostrar nombre legible si el tren es un dict o un string
    for t in trenes_guardados:
        if isinstance(t, dict):
            display = t.get("nombre", str(t))
            value = display
        else:
            display = str(t)
            value = display
        tk.Radiobutton(ventana, text=display, variable=tren_puntito, value=value).pack(anchor="w")  

    def confirmar():  
        seleccionado = tren_puntito.get()
        # buscar y eliminar el elemento correcto (dict o string)
        for item in list(trenes_guardados):  # iteramos sobre copia para poder remover
            if isinstance(item, dict) and item.get("nombre") == seleccionado:
                trenes_guardados.remove(item)
                break
            elif not isinstance(item, dict) and str(item) == seleccionado:
                trenes_guardados.remove(item)
                break

        print("Trenes ahora:", trenes_guardados)  
        ventana.destroy()

    tk.Button(ventana, text="Eliminar", command=confirmar).pack(pady=10)