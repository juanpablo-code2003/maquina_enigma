import utils
import random

class Rotor:
  def __init__(self, inicial = 'A', caracter_click_siguiente: str = None, caracteres_permitidos: str = None, conexiones: list = None) -> None:
    if caracteres_permitidos == None:
      self.caracteres_permitidos = utils.CARACTERES_ASCII
    else:
      self.caracteres_permitidos = caracteres_permitidos.upper()
      
    if len(self.caracteres_permitidos) % 2 != 0:
      raise utils.Error('Los caracteres permitidos del rotor deben ser de cantidad par')
    if not (type(inicial) is str and utils.verificar_caracter(inicial.upper(), self.caracteres_permitidos)):
      raise utils.Error('El caracter inicial ingresado no es permitido')
    
    self.cant_caracteres = len(self.caracteres_permitidos)
    self.inicial = inicial.upper()
    self.num_clicks = self.caracteres_permitidos.index(self.inicial)
    if (type(caracter_click_siguiente) is str and utils.verificar_caracter(caracter_click_siguiente.upper(), self.caracteres_permitidos)):
      self.pos_click_siguiente = self.caracteres_permitidos.index(caracter_click_siguiente.upper())
    else:
      self.pos_click_siguiente = random.randrange(0, self.cant_caracteres)
    
    self.definir_conexiones(conexiones)
    
  def reiniciar(self) -> None:
    self.num_clicks = self.caracteres_permitidos.index(self.inicial)
    
  def __str__(self) -> str:
    return f'Rotor = Inicial: {self.inicial},\n Cant Caracteres: {self.cant_caracteres},\n Clicks: {self.num_clicks},\n Click siguiente: {self.caracteres_permitidos[self.pos_click_siguiente]},\n Caracteres: {self.caracteres_permitidos},\n Conexiones: {self.conexiones}'

  @classmethod
  def verificar_conexiones(cls, conexiones: list, caracteres_permitidos: str) -> bool:
    verificado = (
      conexiones != None 
      and type(conexiones) is list
      and len(conexiones) == len(caracteres_permitidos)
      and len(set(conexiones)) == len(conexiones)
    )
    
    if verificado:
      for con in conexiones:
        if con >= len(caracteres_permitidos):
          verificado = False
          break
    
    return verificado    
      
  def definir_conexiones(self, conexiones: list = None) -> None:
    if conexiones != None:
      if Rotor.verificar_conexiones(conexiones, self.caracteres_permitidos):
        self.conexiones = conexiones
      else:
        raise utils.Error('Las conexiones recibidas no son validas')
    else:
      self.conexiones = list(range(0, self.cant_caracteres))
      random.shuffle(self.conexiones)
      
  def click(self) -> bool:
    click_siguiente_rotor = False
    if self.num_clicks == self.pos_click_siguiente:
      click_siguiente_rotor = True
      
    self.num_clicks += 1
    if self.num_clicks >= self.cant_caracteres:
      self.num_clicks = 0
      
    return click_siguiente_rotor
      
  def encriptar(self, caracter: str) -> str:
    if (type(caracter) is str and utils.verificar_caracter(caracter.upper(), self.caracteres_permitidos)):
      posicion_caracter_entrada = self.caracteres_permitidos.index(caracter)
      try: 
        return self.caracteres_permitidos[self.conexiones[posicion_caracter_entrada + self.num_clicks]]
      except IndexError:
        return self.caracteres_permitidos[self.conexiones[(posicion_caracter_entrada + self.num_clicks) - self.cant_caracteres]]
    else:
      raise utils.Error('El caracter recibido no es permitido')
    
  def encriptar_inverso(self, caracter: str) -> str:
    if (type(caracter) is str and utils.verificar_caracter(caracter.upper(), self.caracteres_permitidos)):
      posicion_caracter_entrada = self.caracteres_permitidos.index(caracter)
      try:
        return self.caracteres_permitidos[self.conexiones.index(posicion_caracter_entrada) - self.num_clicks]
      except ValueError:
        return self.caracteres_permitidos[self.conexiones.index(posicion_caracter_entrada - self.cant_caracteres) - self.num_clicks]
    else:
      raise utils.Error('El caracter recibido no es permitido')
    
    
class Reflector:
  def __init__(self, caracteres_permitidos: str = None, conexiones: list = None) -> None:
    if caracteres_permitidos == None:
      self.caracteres_permitidos = utils.CARACTERES_ASCII
    else:
      self.caracteres_permitidos = caracteres_permitidos.upper()
    
    if len(self.caracteres_permitidos) % 2 != 0:
      raise utils.Error('Los caracteres permitidos del reflector deben ser de cantidad par')
    self.caracteres_permitidos = self.caracteres_permitidos.upper()
    self.cant_caracteres = len(self.caracteres_permitidos)
    self.definir_conexiones(conexiones)
  
  def definir_conexiones(self, conexiones: list = None) -> None:
    if conexiones != None:
      if len(conexiones) == self.cant_caracteres and type(conexiones) is list:
        self.conexiones = conexiones
      else:
        raise utils.Error('Las conexiones recibidas no son validas')
    else:
      self.conexiones = list(range(0, self.cant_caracteres))
      parte1 = list(range(0, self.cant_caracteres // 2))
      parte2 = list(range(self.cant_caracteres // 2, self.cant_caracteres))
      random.shuffle(parte1)
      random.shuffle(parte2)
      
      for i in range(0, len(parte1)):
        self.conexiones[parte1[i]] = parte2[i]
        self.conexiones[parte2[i]] = parte1[i]
      
  def encriptar(self, caracter: str) -> str:
    if (type(caracter) is str and utils.verificar_caracter(caracter.upper(), self.caracteres_permitidos)):
      posicion_caracter_entrada = self.caracteres_permitidos.index(caracter)
      return self.caracteres_permitidos[self.conexiones[posicion_caracter_entrada]]
    else:
      raise utils.Error('El caracter recibido no es permitido')
    