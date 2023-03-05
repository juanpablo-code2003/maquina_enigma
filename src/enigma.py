from src.mecanismos import Rotor, Reflector
import src.utils as utils

class Config:
  def __init__(self, aleatorio = True, num_rotores = 3, cadena_inicial: str = None, cadena_caracteres_vuelta_completa: str = None, caracteres_permitidos: str = None) -> None:
    self.rotores = list()
    self.reflector = object()
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
      conexiones_rotores = [utils.CONEXIONES_ENG_ROTOR_3, utils.CONEXIONES_ENG_ROTOR_2, utils.CONEXIONES_ENG_ROTOR_1]
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
      self.reflector = Reflector(caracteres_permitidos=caracteres_permitidos, conexiones=utils.CONEXIONES_ENG_REFLECTOR)
      
  def reiniciar(self) -> None:
    for rotor in self.rotores:
      rotor.reiniciar()
      
      
def enigma(msg: str, config: Config) -> str:
  if type(msg) is str:
    resultado = ''
    # print('ENCRIPTADO')
    config.reiniciar()
    for caracter in msg:
      if caracter == ' ':
        resultado += caracter
      else:
        resultado_temporal = caracter
        i = 0
        click_siguiente = True
        
        anterior = ''
        
        for rotor in config.rotores:
          if click_siguiente:
            click_siguiente = rotor.click()
          anterior = resultado_temporal
            
          resultado_temporal = rotor.encriptar(resultado_temporal)
          # print(f'Temp: {anterior} -> {resultado_temporal}')
          i += 1
          
        anterior = resultado_temporal
        resultado_temporal = config.reflector.encriptar(resultado_temporal)
        # print(f'Temp: {anterior} -> {resultado_temporal}')
        
        
        i = len(config.rotores) - 1
        for rotor in reversed(config.rotores):
          anterior = resultado_temporal
          resultado_temporal = rotor.encriptar_inverso(resultado_temporal)
          # print(f'Temp: {anterior} -> {resultado_temporal}')
          i -= 1
          
        resultado += resultado_temporal
        # print('...')
    
    return resultado
  else:
    raise utils.Error('Configuracion o mensaje invalido')
  
    
      
