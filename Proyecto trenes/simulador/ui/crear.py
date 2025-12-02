import tkinter as tk
from datos import rutas_guardadas, estaciones_guardadas, trenes_guardados

#generador
import datetime as dt

class GenerarTrenes:
    def __init__(self, vagones = 5, capacidad=1000 , fecha_inicial: dt.datetime = dt.datetime(2025,1,1)):
        self.vagones=vagones
        self.capacidad=capacidad
        self.tren = []
        for i in range(vagones):
            self.tren.append([])
        self.fecha_inicial=fecha_inicial
        self.min_pasajeros=int(capacidad*0.1)  #minimo
        self.max_pasajeros=int(capacidad*0.2)  #el max

    def llenar_tren(self):  #llenar el tren 
        import random
        for i in range(self.vagones):
            pasajeros = random.randint(self.min_pasajeros, self.max_pasajeros)
            self.tren[i] = [f'pasajero_{j+1}' for j in range(pasajeros)]

    def mostrar_tren(self):  # mostrar
        i= 1   
        for vag in self.tren:
            print(f'Vagon {i}:', vag)
            i+= 1



def crear_estacion(ventanafaz):  
    ventana_estacion = tk.Toplevel(ventanafaz)
    ventana_estacion.title("Crear estacion")
    ventana_estacion.geometry("300x250")  
    tk.Label(ventana_estacion, text= "Nombre de la estacion:").pack(pady =  5)
    texto=tk.Text(ventana_estacion, height = 2, width=30)
    texto.pack(pady = 5)
    #numero de vias
    tk.Label(ventana_estacion, text="Número de vias:").pack(pady =5)
    vias=tk.Entry(ventana_estacion)
    vias.pack(pady=5)

    def guardar_estacion():
        try:
            nombre=texto.get("1.0","end-1c")
            vias_valor=vias.get()
            if not nombre.strip():
                raise ValueError("Sin nombre")

            if not vias_valor.isdigit():
                raise ValueError("nombre Invalido")  
            if int(vias_valor) < 1:
                raise ValueError("Deben existir vias, almenos 1")  
            vias_int = int(vias_valor)
            estacion ={  #volvemos estacion como un diccionario
                "nombre": nombre.strip(),
                "vias": vias_int,       
                "vias_ocupadas": []}
            estaciones_guardadas.append(estacion)  
            print("Estaciones guardadas: ", estaciones_guardadas)
        except Exception as e:  
            print("Error no se pudo crear la estacion", e)  
            return 
        ventana_estacion.destroy()
    tk.Button(ventana_estacion, text="Guardar estación", command = guardar_estacion).pack(pady=10)


def crear_ruta(ventanafaz):  
    ventana_ruta= tk.Toplevel(ventanafaz)
    ventana_ruta.title("Crear ruta")
    ventana_ruta.geometry("300x200")
    tk.Label(ventana_ruta, text="Nombre de la ruta:").pack(pady=5)
    texto = tk.Text(ventana_ruta, height=2, width=30)
    texto.pack(pady=5)

    def guardar_ruta():
        try:
            nombre = texto.get("1.0", "end-1c")
            if not nombre.strip():
                raise ValueError("ruta sin nombre")  
            if nombre.strip() in rutas_guardadas:
                raise ValueError("La ruta ya esta creada")
            rutas_guardadas.append(nombre.strip())
            print("Rutas guardadas:", rutas_guardadas)
        except Exception as e:  
            print("Error no se pudo crear la ruta", e)  
            return 
        ventana_ruta.destroy()
    tk.Button(ventana_ruta, text="Guardar ruta", command=guardar_ruta).pack(pady=10)


def crear_tren(ventanafaz):
    ventana_tren = tk.Toplevel(ventanafaz)
    ventana_tren.title("Crear tren")
    ventana_tren.geometry("400x600")  
    tk.Label(ventana_tren, text="Crear tren").pack(pady = 5)
    tk.Label(ventana_tren, text="Nombre del tren:").pack(pady = 5)
    nombre_text = tk.Text(ventana_tren, height = 2, width = 40)
    nombre_text.pack(pady = 5)
    # guarda rutas
    tk.Label(ventana_tren, text="Ruta:").pack(pady=5)
    if rutas_guardadas:
        ruta_puntito = tk.StringVar(ventana_tren)
        for r in rutas_guardadas:
            tk.Radiobutton(ventana_tren, text=r, variable=ruta_puntito, value=r).pack(anchor="w")
    else:
        tk.Label(ventana_tren, text="No existe esta  ruta").pack(pady=5)
        ruta_puntito =None
        
     # guardar estación
    tk.Label(ventana_tren, text="Estacion:").pack(pady=5)
    if estaciones_guardadas:
        estacion_puntito=tk.StringVar(ventana_tren) #puntito marcado
        for e in estaciones_guardadas:
            tk.Radiobutton(ventana_tren, text=e["nombre"], variable=estacion_puntito, value=e["nombre"]).pack(anchor="w")
    else:
        tk.Label(ventana_tren, text="No existe esta estación").pack(pady=5)
        estacion_puntito=None
    #selección de viaas
    tk.Label(ventana_tren, text="Vía:").pack(pady=5)
    via_puntito =tk.StringVar(ventana_tren)
    vias_frame= tk.Frame(ventana_tren)
    vias_frame.pack()
    
    def actualizar_vias(*args):  #este es importate por que es para aceptar cualqueir agurmenteo 
        for widget in vias_frame.winfo_children():
            widget.destroy()
        estacion_nombre = estacion_puntito.get() if estacion_puntito else None
        if estacion_nombre:
            estacion = next((est for est in estaciones_guardadas if est["nombre"]==estacion_nombre), None)
            if estacion:
                for i in range(1, estacion["vias"]+1):
                    if i not in estacion["vias_ocupadas"]:
                        tk.Radiobutton(vias_frame, text=str(i), variable=via_puntito, value=str(i)).pack(anchor="w")

    if estacion_puntito: 
        estacion_puntito.trace_add("write", actualizar_vias)  
    actualizar_vias()  #iniciar
    #generador como objeto 
    tren_generado = GenerarTrenes(vagones=5, capacidad=20)  
    tren_generado.llenar_tren()  #llenamos con pasajeros 

    def mostrar_texto():
        try:
            nombre=nombre_text.get("1.0", "end-1c")
            if not nombre.strip():
                raise ValueError("Tren sin nombre")  
            ruta_sel =ruta_puntito.get() if ruta_puntito else None
            if not ruta_sel:
                raise ValueError("se debe seleccionar un tren") 
            estacion_nombre= estacion_puntito.get() if estacion_puntito else None
            if not estacion_nombre:
                raise ValueError("se debe seleccionar una estacion")  
            via_valor = via_puntito.get()
            if not via_valor:
                raise ValueError("Se debe seleccionar una vía")  
            try:
                via_sel = int(via_valor)
            except:
                raise ValueError("La via no se pudo seleccionar")
            estacion=None
            for ess in estaciones_guardadas:
                if ess["nombre"] == estacion_nombre:
                    estacion = ess
                    break
            if estacion and via_sel in estacion["vias_ocupadas"]:
                raise ValueError("La via esta ocupada") 
        except Exception as e:  
            print("ERROR al crear tren:", e) 
            return



        print("Nombre:", nombre)
        #seleccio
        ruta_sel=ruta_puntito.get() if ruta_puntito else None
        estacion_nombre =estacion_puntito.get() if estacion_puntito else None
        via_sel= int(via_puntito.get()) if via_puntito.get() else None  
        if ruta_sel:
            print("Ruta:", ruta_sel)
        if estacion_nombre:
            print("Estación:", estacion_nombre)
        if via_sel:
            print("Vía asignada:", via_sel)  
        print("Pasajeros generados por vagón:")  
        tren_generado.mostrar_tren()  

        #guardar tren
        if nombre.strip():
            tren = {"nombre": nombre.strip(),
                "ruta": ruta_sel,
                "estacion": estacion_nombre,
                "via": via_sel,
                "pasajeros": tren_generado.tren }
            trenes_guardados.append(tren)
            #en caso de estar ocupado
            if estacion_nombre and via_sel:
                estacion = next((est for est in estaciones_guardadas if est["nombre"] == estacion_nombre), None)
                if estacion:
                    estacion["vias_ocupadas"].append(via_sel)
            print("Trenes:", trenes_guardados)  

        ventana_tren.destroy()
    tk.Button(ventana_tren, text="Mostrar datos", command=mostrar_texto).pack(pady=10)
