import sys
import os
import random

path = os.path.abspath('src/')
sys.path.append(path)

import enigma
import utils

def crear_configuracion(**kwargs):
  config_dict = {
    'aleatorio': kwargs.get('aleatorio') if isinstance(kwargs.get('aleatorio'), bool) else True,
    'num_rotores': kwargs.get('num_rotores'),
    'cadena_inicial': kwargs.get('cadena_inicial') if kwargs.get('cadena_inicial') != '' else None,
    'cadena_caracteres_vuelta_completa': kwargs.get('cadena_caracteres_vuelta_completa') if kwargs.get('cadena_caracteres_vuelta_completa') != '' else None,
    'caracteres_permitidos': utils.ALFABETO_ENG if not kwargs.get('aleatorio') else utils.CARACTERES_ASCII,
    'conexiones_rotores': utils.CONEXIONES_ROTORES_ENG if not kwargs.get('aleatorio') else None,
    'conexiones_reflector': utils.CONEXIONES_REFLECTOR_ENG if not kwargs.get('aleatorio') else None
  }
  configuracion = enigma.Config(**config_dict.copy())
  
  config_dict['aleatorio'] = False
  config_dict['num_rotores'] = configuracion.get_num_rotores()
  config_dict['cadena_inicial'] = configuracion.get_cadena_inicial()
  config_dict['cadena_caracteres_vuelta_completa'] = configuracion.get_cadena_caracteres_vuelta_completa()
  config_dict['caracteres_permitidos'] = configuracion.caracteres_permitidos
  config_dict['conexiones_rotores'] = configuracion.get_conexiones_rotores()
  config_dict['conexiones_reflector'] = configuracion.get_conexiones_reflector()
  enigma.guardar_configuracion(config_dict)
  
def encriptar_mensaje(**kwargs):
  configuracion = enigma.Config(**enigma.get_configuracion())
  return enigma.enigma(msg=kwargs.get('mensaje'), config=configuracion)

def cadena_random(rotores_aleatorios: bool, num_rotores: int):
    cadena = ''
    caracteres_permitidos = utils.ALFABETO_ENG if not rotores_aleatorios else utils.CARACTERES_ASCII
    for _ in range(0, num_rotores):
      cadena += random.choice(caracteres_permitidos)
      
    return cadena
  
