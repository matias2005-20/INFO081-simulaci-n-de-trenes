import tkinter as tk
from PIL import Image, ImageTk
from config import titulo, alto, ancho, color
from ui.menu import abrir_menu

# Ventana principal
ventanain = tk.Tk()
ventanain.title(titulo) #init
ventanain.geometry(f"{ancho}x{alto}") #importado de init
ventanain.configure(bg=color) #color en el init 

tk.Button(ventanain, text="Iniciar", command=lambda: abrir_menu(ventanain)).pack(pady=60) 

ventanain.mainloop()