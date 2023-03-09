from tkinter import *
from tkinter import ttk

import frames

class VentanaPrincipal():
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Máquina Enigma')

    menu = ttk.Notebook(self.root)

    frame_config_maquina = frames.frame_config_maquina(menu)
    frame_encriptar_texto = frames.frame_encriptar_texto(menu)
    frame_encriptar_archivo = frames.frame_encriptar_archivo(menu)


    menu.add(frame_config_maquina, text='Configuración')
    menu.add(frame_encriptar_texto, text='Encriptar Mensaje')
    menu.add(frame_encriptar_archivo, text='Encriptar Archivo')

    self.root.columnconfigure(0, weight=1)
    self.root.rowconfigure(0, weight=1)

    menu.pack(padx=10, pady=10)
    
  def show(self):
    self.root.mainloop()