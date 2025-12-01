import json #formato en el que guradamos en diccionarios
from datos import rutas_guardadas, estaciones_guardadas, trenes_guardados

ARCHIVO = "datos_guardados.json"

def guardar_datos():
    datos = {"rutas": rutas_guardadas,"estaciones": estaciones_guardadas,"trenes": trenes_guardados}

    try:
        with open(ARCHIVO, "w", encoding = "utf-8") as f:
            json.dump(datos, f, indent =4, ensure_ascii= False) #para convertirlo en archivos
        print("Datos guardados.")
    except Exception as e:
        print("Error al guardar:", e)



def cargar_datos():
    global rutas_guardadas, estaciones_guardadas, trenes_guardados
    try:
        with open(ARCHIVO, "r", encoding = "utf-8") as f:
            datos =json.load(f)
        rutas_guardadas.clear() #borramos dartos para colocar los nuevos
        print("Rutas:", rutas_guardadas)
        estaciones_guardadas.clear()
        print("Estaciones:", estaciones_guardadas)
        print("Rutas:", rutas_guardadas)
        trenes_guardados.clear()
        print("Trenes:", trenes_guardados)
        rutas_guardadas.extend(datos.get("rutas", []))

        estaciones_guardadas.extend(datos.get("estaciones", []))
        
        trenes_guardados.extend(datos.get("trenes", []))
        print("datos cargados: ")
    except FileNotFoundError:
        print("No existe archivo por ahora.")
    except Exception as e:
        print("Error al cargar:", e)