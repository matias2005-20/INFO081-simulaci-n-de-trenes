import json #formato en el que guradamos en diccionarios
from datos import rutas_guardadas, estaciones_guardadas, trenes_guardados

ARCHIVO = "datos_guardados.json"

def guardar_datos():
    """Guarda rutas, estaciones y trenes en un archivo JSON."""
    datos = {
        "rutas": rutas_guardadas,
        "estaciones": estaciones_guardadas,
        "trenes": trenes_guardados
    }

    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("Datos guardados correctamente.")
    except Exception as e:
        print("Error al guardar:", e)



def cargar_datos():
    global rutas_guardadas, estaciones_guardadas, trenes_guardados

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)

        rutas_guardadas.clear()
        estaciones_guardadas.clear()
        trenes_guardados.clear()

        rutas_guardadas.extend(datos.get("rutas", []))
        estaciones_guardadas.extend(datos.get("estaciones", []))
        trenes_guardados.extend(datos.get("trenes", []))

        print("Datos cargados correctamente:")
        print("Rutas:", rutas_guardadas)
        print("Estaciones:", estaciones_guardadas)
        print("Trenes:", trenes_guardados)

    except FileNotFoundError:
        print("No hay archivo para cargar todavía.")
    except Exception as e:
        print("Error al cargar:", e)