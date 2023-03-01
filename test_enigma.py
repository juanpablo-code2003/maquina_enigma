import unittest
import enigma
import utils
import random


class TestEnigma(unittest.TestCase):
  # Este test requiere un tiempo de ejecucion mayor a 20 segundos
  @unittest.skip('Ejecucion larga')
  def test_enigma_aleatorio_hasta_1000_rotores(self):
    mensaje = 'MENSAJE'
    for num_rotores in range(1, 1000):
      configuracion = enigma.Config(aleatorio=True, num_rotores=num_rotores)
      encriptado = enigma.enigma(msg=mensaje, config=configuracion)
      desencriptado = enigma.enigma(msg=encriptado, config=configuracion)
      self.assertEqual(mensaje, desencriptado, {'num_rotores': num_rotores})
      
  def test_enigma_aleatorio_determinados_caracteres(self):
    mensaje = 'MENSAJE'
    num_rotores = random.randrange(1, 1001)
    configuracion = enigma.Config(aleatorio=True, num_rotores=num_rotores, caracteres_permitidos=utils.ALFABETO_ENG)
    encriptado = enigma.enigma(msg=mensaje, config=configuracion)
    desencriptado = enigma.enigma(msg=encriptado, config=configuracion)
    self.assertEqual(mensaje, desencriptado, {'num_rotores': num_rotores})
    
  def test_enigma_definido(self):
    mensaje = 'MENSAJE'
    configuracion = enigma.Config(aleatorio=False, cadena_inicial='ASD', cadena_caracteres_vuelta_completa='VFG', caracteres_permitidos=utils.ALFABETO_ENG)
    encriptado = enigma.enigma(msg=mensaje, config=configuracion)
    desencriptado = enigma.enigma(msg=encriptado, config=configuracion)
    rotores_str = list()
    for r in configuracion.rotores:
      rotores_str.append(r.__str__())
    self.assertEqual(mensaje, desencriptado, rotores_str)
    
    
    