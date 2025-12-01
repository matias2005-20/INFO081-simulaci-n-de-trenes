import tkinter as tk
from datos import trenes_guardados

def mostrar_datos_tren(ventanafaz):
    if not trenes_guardados:
        print("no hay trenes")
        return

    ven = tk.Toplevel(ventanafaz)
    ven.title("Tren")
    ven.geometry("300x300")

    tk.Label(ven, text="selecciona el tren: ").pack(pady=5)

    tren_var=tk.StringVar(ven)

    for t in trenes_guardados:
        try:
            n=t.get("nombre", str(t)) 
        except:  
            n=str(t)  
        tk.Radiobutton(ven, text= n, variable = tren_var, value = n).pack(anchor = "w")

    def mostrar():
        sel = tren_var.get()
        for t in trenes_guardados:
            try:
                if t.get("nombre") == sel:
                    print("Nombre del tren:", t['nombre'])
                    print("Ruta del tren:", t['ruta'])
                    print("Estacion:", t['estacion'])
                    try:
                        if "vias" in t["estacion"]:
                            print("Vias disponibles:", t["estacion"]["vias"])
                    except:  
                        pass
                    break
            except: 
                continue

    tk.Button(ven, text="Mostrar", command=mostrar).pack(pady=10)