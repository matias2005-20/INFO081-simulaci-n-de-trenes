import datetime as dt
from generador import GeneradorUniforme

class generatrenes:
     def __init__(self,vagones=int, capacidad=int,fecha_inicial: dt.datetime = dt.datetime(2025, 1, 1)):
          self.vagones = vagones
          self.capacidad = capacidad 
          self.tren = [[] for _ in range(vagones)]
          self.fecha_inicial = fecha_inicial
          self.generador = GeneradorUniforme(0, capacidad - 1)
     def llenar_tren(self):
          for i in range(self.vagones):
               pasajeros =self.generador.generar()
          self.tren[i] = [f''pasajero_{j+1}''for j in range(pasajeros)]
     def mostrar_tren(self):
          for i,vag in enumerate(self.tren):
               print(f''Vagon {i+1}:'', vag)
               

           


   
