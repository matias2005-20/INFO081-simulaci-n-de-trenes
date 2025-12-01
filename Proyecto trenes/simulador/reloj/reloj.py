import tkinter as tk
import time

class Reloj:
    def __init__(self, parent, x=400, y=20): 
        self.parent = parent #actrualizar el rejo
        self.label = tk.Label(parent, text="", font=("Helvetica", 14), fg="green", bg="white") # mucho mas grande: font=("Helvetica", 14)
        self.label.pack(side="right", padx=0, pady=10)
        self.actualizar_reloj()

    def actualizar_reloj(self):
        hora_actual = time.strftime("%H:%M:%S")  
        self.label.config(text=hora_actual)
        self.parent.after(1000, self.actualizar_reloj)  