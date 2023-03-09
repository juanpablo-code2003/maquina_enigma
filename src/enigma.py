import json
import os

from mecanismos import Rotor, Reflector
import utils

class Config:
  def __init__(self, aleatorio = True, num_rotores = 3, cadena_inicial: str = None, cadena_caracteres_vuelta_completa: str = None, caracteres_permitidos: str = None, conexiones_rotores: list = None, conexiones_reflector: list = None) -> None:
    self.rotores = list()
    self.reflector = object()
    self.caracteres_permitidos = caracteres_permitidos
    if aleatorio == True:
      for i in range(0, num_rotores):
        parametros = dict()
        parametros['caracteres_permitidos'] = caracteres_permitidos
        if cadena_inicial != None:
          parametros['inicial'] = cadena_inicial[i]
        if cadena_caracteres_vuelta_completa != None:
          parametros['caracter_click_siguiente'] = cadena_caracteres_vuelta_completa[i]
          
        self.rotores.append(Rotor(**parametros))
      self.reflector = Reflector(caracteres_permitidos=caracteres_permitidos)
    else:
      if conexiones_rotores == None:
        conexiones_rotores = utils.CONEXIONES_ROTORES_ENG
      iniciales = list()
      caract_click_siguiente = list()
      if cadena_inicial != None:
        iniciales = list(cadena_inicial)
        iniciales.reverse()
      if cadena_caracteres_vuelta_completa != None:
        caract_click_siguiente = list(cadena_caracteres_vuelta_completa)
        caract_click_siguiente.reverse()
        
      for i in range(0, len(conexiones_rotores)):
        self.rotores.append(Rotor(
          inicial=iniciales[i], 
          caracter_click_siguiente=caract_click_siguiente[i], 
          caracteres_permitidos=caracteres_permitidos, 
          conexiones=conexiones_rotores[i]
        ))
        
      if conexiones_reflector == None:
        conexiones_reflector = utils.CONEXIONES_REFLECTOR_ENG
      self.reflector = Reflector(caracteres_permitidos=caracteres_permitidos, conexiones=conexiones_reflector)
      
  def reiniciar(self) -> None:
    for rotor in self.rotores:
      rotor.reiniciar()
      
  def get_num_rotores(self):
    return len(self.rotores)
      
  def get_conexiones_rotores(self):
    conexiones = list()
    for rotor in self.rotores:
      conexiones.append(rotor.conexiones)
    return conexiones
      
  def get_conexiones_reflector(self):
    return self.reflector.conexiones
  
  def get_cadena_inicial(self):
    cadena = ''
    for rotor in reversed(self.rotores):
      cadena += rotor.inicial
    return cadena
  
  def get_cadena_caracteres_vuelta_completa(self):
    cadena = ''
    for rotor in reversed(self.rotores):
      cadena += self.caracteres_permitidos[rotor.pos_click_siguiente]
    return cadena
      
      
def enigma(msg: str, config: Config) -> str:
  if type(msg) is str:
    resultado = ''
    config.reiniciar()
    for caracter in msg:
      if caracter == '\n':
        resultado_temporal = '\n'
      else:
        resultado_temporal = caracter
        click_siguiente = True
        
        for rotor in config.rotores:
          if click_siguiente:
            click_siguiente = rotor.click()
          resultado_temporal = rotor.encriptar(resultado_temporal)
          
        resultado_temporal = config.reflector.encriptar(resultado_temporal)
        
        for rotor in reversed(config.rotores):
          resultado_temporal = rotor.encriptar_inverso(resultado_temporal)
        
      resultado += resultado_temporal
    
    return resultado
  else:
    raise utils.Error('Configuracion o mensaje invalido')
  

def guardar_configuracion(config: dict, nombre_archivo = ''):
  json_str = json.dumps(config)
  archivo = open(os.path.abspath(f'src/archivos/{nombre_archivo}_config.json'), 'w')
  archivo.write(json_str)
  archivo.close()
  
def get_configuracion(nombre_archivo = ''):
  archivo = open(os.path.abspath(f'src/archivos/{nombre_archivo}_config.json'), 'r')
  json_str = archivo.readline()
  archivo.close()
  return json.loads(json_str)
  
  
    
      
