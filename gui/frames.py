from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import random

import eventos

path = os.path.abspath('src/')
sys.path.append(path)

import utils

def frame_config_maquina(parent):
  frame_config_maquina = ttk.Frame(parent, padding='3 3 12 12')
  frame_config_maquina.grid(column=0, row=0, sticky=(N, W, E, S))
  
  variables = {
    'aleatorio': BooleanVar(),
    'num_rotores': IntVar(),
    'cadena_inicial': StringVar(),
    'cadena_vuelta_completa': StringVar()
  }
  
  def handle_change_aleatorio(input_num_rotores, variables):
    if not variables['aleatorio'].get():
      variables['num_rotores'].set(3)
      input_num_rotores.config(state='disabled')
    else:
      input_num_rotores.config(state='normal')

  input_aleatorio = ttk.Checkbutton(
    frame_config_maquina, 
    text='Rotores Aleatorios', 
    offvalue=False, 
    onvalue=True, 
    variable=variables['aleatorio'], 
    command=lambda: handle_change_aleatorio(input_num_rotores=input_num_rotores, variables=variables))
  input_aleatorio.grid(column=2, row=1, sticky=(W))
  variables['aleatorio'].set(True)
  
  label_num_rotores = ttk.Label(frame_config_maquina, text='Número Rotores')
  label_num_rotores.grid(column=1, row=2, sticky=(E))
  input_num_rotores = ttk.Spinbox(frame_config_maquina, from_=1.0, to=1000.0, textvariable=variables['num_rotores'])
  input_num_rotores.grid(column=2, row=2, sticky=(W))
  
  def cadena_random(variables, str_variable):
    cadena = eventos.cadena_random(variables['aleatorio'].get(), variables['num_rotores'].get())
    variables[str_variable].set(cadena)
  
  label_cadena_inicial = ttk.Label(frame_config_maquina, text='Cadena Inicial')
  label_cadena_inicial.grid(column=1, row=3, sticky=(E))
  input_cadena_inicial = ttk.Entry(frame_config_maquina, textvariable=variables['cadena_inicial'])
  input_cadena_inicial.grid(column=2, row=3, sticky=(W))
  
  btn_cadena_inicial_aleatoria = ttk.Button(frame_config_maquina, text='Aleatoria')
  btn_cadena_inicial_aleatoria.bind('<ButtonPress-1>', lambda e: cadena_random(variables, 'cadena_inicial'))
  btn_cadena_inicial_aleatoria.grid(column=3, row=3, sticky=(W))
  
  label_cadena_vuelta_completa = ttk.Label(frame_config_maquina, text='Cadena Vuelta Completa')
  label_cadena_vuelta_completa.grid(column=1, row=4, sticky=(E))
  input_cadena_vuelta_completa = ttk.Entry(frame_config_maquina, textvariable=variables['cadena_vuelta_completa'])
  input_cadena_vuelta_completa.grid(column=2, row=4, sticky=(W))
  
  btn_cadena_vuelta_aleatoria = ttk.Button(frame_config_maquina, text='Aleatoria')
  btn_cadena_vuelta_aleatoria.bind('<ButtonPress-1>', lambda e: cadena_random(variables, 'cadena_vuelta_completa'))
  btn_cadena_vuelta_aleatoria.grid(column=3, row=4, sticky=(W))
  
  label_mensaje = ttk.Label(frame_config_maquina, text='*Con rotores no aleatorios, las conexiones estan preestablecidas\n y el alfabeto será inglés mayúsculas sin espacio (como el tarro de Pringles).', justify='center')
  label_mensaje.grid(column=1, row=5, columnspan=3)
  
  def configurar(variables):
    try:
      eventos.crear_configuracion(
        aleatorio=variables['aleatorio'].get(),
        num_rotores=variables['num_rotores'].get(),
        cadena_inicial=variables['cadena_inicial'].get(),
        cadena_caracteres_vuelta_completa=variables['cadena_vuelta_completa'].get()
      )
      messagebox.showinfo(message='Configuración almacenada')
    except utils.Error as err:
      messagebox.showerror(message=err)
      

  btn_crear_config = ttk.Button(frame_config_maquina, text='Configurar máquina')
  btn_crear_config.grid(column=1, row=6, columnspan=3)
  btn_crear_config.bind('<ButtonPress-1>', lambda e: configurar(variables))
  
  for child in frame_config_maquina.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
  
  return frame_config_maquina


def frame_encriptar_texto(parent):
  frame_encriptar_texto = ttk.Frame(parent, padding='3 3 12 12')
  frame_encriptar_texto.grid(column=0, row=0, sticky=(N, W, E, S))
  
  variables = {
    'mensaje': StringVar(),
    'encriptado': StringVar()
  }
  
  label_mensaje = ttk.Label(frame_encriptar_texto, text='Mensaje a encriptar')
  label_mensaje.grid(column=1, row=1, sticky=(W))
  input_mensaje = ttk.Entry(frame_encriptar_texto, textvariable=variables['mensaje'])
  input_mensaje.grid(column=1, row=2, sticky=(E, W))
  
  def encriptar(msg, enc):
    try:
      enc.set(eventos.encriptar_mensaje(mensaje=msg.get()))
    except utils.Error as err:
      messagebox.showerror(message=err)
  
  btn_enigma = ttk.Button(frame_encriptar_texto, text='Enigma')
  btn_enigma.grid(column=1, row=3)
  btn_enigma.bind('<ButtonPress-1>', lambda e: encriptar(variables['mensaje'], variables['encriptado']))
  
  label_encriptado = ttk.Label(frame_encriptar_texto, text='Resultado')
  label_encriptado.grid(column=1, row=4, sticky=(W))
  input_encriptado = ttk.Entry(frame_encriptar_texto, textvariable=variables['encriptado'])
  input_encriptado.grid(column=1, row=5, sticky=(E, W))
  
  label_aviso = ttk.Label(frame_encriptar_texto, text='La configuración está almacenada en el archivo: /src/archivos/_config.json')
  label_aviso.grid(column=1, row=6)
  
  return frame_encriptar_texto


def frame_encriptar_archivo(parent):
  frame_encriptar_archivo = ttk.Frame(parent, padding='3 3 12 12')
  frame_encriptar_archivo.grid(column=0, row=0, sticky=(N, W, E, S))
  
  variables = {
    'texto_archivo': StringVar(),
    'texto_encriptado': StringVar()
  }
  
  def pedir_archivo(cuadro_texto):
    try:
      archivo = filedialog.askopenfile(filetypes=[('Archivos txt', '*.txt')])
      if archivo != None and archivo != '':
        texto = archivo.read()
        archivo.close()
        cuadro_texto.delete('1.0', 'end')
        cuadro_texto.insert('1.0', texto)
    except Exception as err:
      messagebox.showerror(message=err)
      
  
  label_archivo_texto = ttk.Label(frame_encriptar_archivo, text='Seleccionar el archivo (.txt)')
  label_archivo_texto.grid(column=1, row=1, sticky=(E))
  btn_abrir_archivo_texto = ttk.Button(frame_encriptar_archivo, text='Abrir')
  btn_abrir_archivo_texto.bind('<ButtonPress-1>', lambda e: pedir_archivo(cuadro_texto))
  btn_abrir_archivo_texto.grid(column=2, row=1, sticky=(W))
  
  cuadro_texto = Text(frame_encriptar_archivo, width=50, height=8)
  cuadro_texto.grid(column=1, row=2, columnspan=2)
  ys = ttk.Scrollbar(frame_encriptar_archivo, orient='vertical', command=cuadro_texto.yview)
  cuadro_texto['yscrollcommand'] = ys.set
  ys.grid(column=1, row=2, columnspan=2, sticky = 'nse')
  
  def encriptar_texto(cuadro_texto):
    try:
      enc = eventos.encriptar_mensaje(mensaje=cuadro_texto.get('1.0', 'end'))
      cuadro_texto.delete('1.0', 'end')
      cuadro_texto.insert('1.0', enc)
    except utils.Error as err:
      messagebox.showerror(message=err)
  
  btn_encriptar_texto = ttk.Button(frame_encriptar_archivo, text='Enigma')
  btn_encriptar_texto.bind('<ButtonPress-1>', lambda e: encriptar_texto(cuadro_texto))
  btn_encriptar_texto.grid(column=1, row=3, columnspan=2)
  
  def guardar_encriptacion(cuadro_texto):
    try:
      archivo = filedialog.asksaveasfile(title='Guardar como', filetypes=[('Archivos txt', '*.txt')])
      if archivo != None and archivo != '':
        archivo.write(cuadro_texto.get('1.0', 'end'))
        archivo.close()
    except Exception as err:
      messagebox.showerror(message=err)
  
  btn_guardar_encriptacion = ttk.Button(frame_encriptar_archivo, text='Guardar Encriptación')
  btn_guardar_encriptacion.bind('<ButtonPress-1>', lambda e: guardar_encriptacion(cuadro_texto))
  btn_guardar_encriptacion.grid(column=1, row=4, columnspan=2)
  
  return frame_encriptar_archivo