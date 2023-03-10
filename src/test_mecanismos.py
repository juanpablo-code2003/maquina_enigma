import unittest
import random

import utils

from mecanismos import Rotor, Reflector

class TestRotorAleatorio(unittest.TestCase):
  def test_inicial_invalido(self):
    pruebas = ['^', 'abc', '|']
    for p in pruebas:
      with self.assertRaises(utils.Error):
        rotor = Rotor(p)
        
  def test_inicial_valido(self):
    for c in utils.CARACTERES_ASCII:
      rotor = Rotor(c)
      self.assertEqual(rotor.inicial, c)
      self.assertGreaterEqual(rotor.pos_click_siguiente, 0)
      self.assertLess(rotor.pos_click_siguiente, utils.CANT_CARACTERES_ASCII)
      
  def test_disposicion_aleatoria(self):
    rotor = Rotor('A')
    self.assertIsInstance(rotor.conexiones, list)
    self.assertEqual(len(rotor.conexiones), utils.CANT_CARACTERES_ASCII)
    
    set_conexiones = set(rotor.conexiones)
    self.assertEqual(len(set_conexiones), len(rotor.conexiones))
      
  def test_click_reinicio_clicks(self):
    rotor = Rotor('_')
    rotor.num_clicks = utils.CANT_CARACTERES_ASCII - 1
    rotor.click()
    self.assertEqual(rotor.num_clicks, 0)
    
  def test_click_retorno_siguiente_click(self):
    rotor = Rotor('4')
    rotor.pos_click_siguiente = utils.CARACTERES_ASCII.index('4')
    self.assertTrue(rotor.click())
    self.assertFalse(rotor.click())
    self.assertFalse(rotor.click())
    self.assertFalse(rotor.click())
    
  def test_encriptacion_invalida(self):
    rotor = Rotor('!')
    pruebas = ['^', 'abc', '|']
    for p in pruebas:
      with self.assertRaises(utils.Error):
        rotor.click()
        rotor.encriptar(p)
        
  def test_encriptacion(self):
    rotor = Rotor('T')
    caracter = random.choice(utils.CARACTERES_ASCII)
    
    rotor.click()
    resultado1 = rotor.encriptar(caracter)
    self.assertIsInstance(resultado1, str)
    self.assertEqual(len(resultado1), 1)
    
    rotor.click()
    resultado2 = rotor.encriptar(caracter)
    self.assertIn(resultado2, utils.CARACTERES_ASCII)
    self.assertEqual(len(resultado2), 1)
    
    rotor.click()
    resultado3 = rotor.encriptar(caracter)
    self.assertEqual(len(resultado3), 1)
    
    self.assertNotEqual(resultado3, resultado1)
    self.assertNotEqual(resultado3, resultado2)
    
  def test_encriptacion_repetida_una_vuelta(self):
    rotor = Rotor(utils.CARACTERES_ASCII[0])
    resultado1 = rotor.encriptar('A')
    for _ in utils.CARACTERES_ASCII:
      rotor.click()
    resultado2 = rotor.encriptar('A')
    self.assertEqual(resultado1, resultado2)
    
  def test_encriptacion_inversa(self):
    caracter = random.choice(utils.CARACTERES_ASCII)
    rotor = Rotor('G')
    
    rotor.click()
    resultado1 = rotor.encriptar_inverso(caracter)
    self.assertIsInstance(resultado1, str)
    self.assertEqual(len(resultado1), 1)
    
    rotor.click()
    resultado2 = rotor.encriptar_inverso(caracter)
    self.assertIn(resultado2, utils.CARACTERES_ASCII)
    self.assertEqual(len(resultado2), 1)
    
    rotor.click()
    resultado3 = rotor.encriptar_inverso(caracter)
    self.assertEqual(len(resultado3), 1)
    
    self.assertNotEqual(resultado3, resultado1, rotor)
    self.assertNotEqual(resultado3, resultado2, rotor)
    
  def test_encriptacion_inversa_repetida_una_vuelta(self):
    rotor = Rotor(utils.CARACTERES_ASCII[0])
    resultado1 = rotor.encriptar_inverso('A')
    for _ in utils.CARACTERES_ASCII:
      rotor.click()
    resultado2 = rotor.encriptar_inverso('A')
    self.assertEqual(resultado1, resultado2)
    
  def test_comparacion_encriptaciones(self):
    rotor = Rotor(random.choice(utils.CARACTERES_ASCII))
    
    for c in utils.CARACTERES_ASCII:
      normal = rotor.encriptar(c)
      inverso = rotor.encriptar_inverso(normal)
      self.assertEqual(c, inverso, {'clicks': rotor.num_clicks, 'conexiones': rotor.conexiones})
      
      
class TestRotorConfigurado(unittest.TestCase):
  def test_inicial_valido(self):
    for c in utils.ALFABETO_ENG:
      rotor = Rotor(c, caracteres_permitidos=utils.ALFABETO_ENG)
      self.assertEqual(rotor.inicial, c)
      self.assertGreaterEqual(rotor.pos_click_siguiente, 0)
      self.assertLess(rotor.pos_click_siguiente, utils.CANT_ALFABETO_ENG)
      
  def test_encriptacion(self):
    rotor = Rotor(inicial=random.choice(utils.ALFABETO_ENG), caracteres_permitidos=utils.ALFABETO_ENG, conexiones=utils.CONEXIONES_ENG_ROTOR_1)
    
    for c in utils.ALFABETO_ENG:
      normal = rotor.encriptar(c)
      inverso = rotor.encriptar_inverso(normal)
      self.assertEqual(c, inverso, {'clicks': rotor.num_clicks, 'conexiones': rotor.conexiones})
             
    
class TestReflector(unittest.TestCase):
  def test_encriptacion_invalida(self):
    reflector = Reflector()
    pruebas = ['^', 'abc', '|']
    for p in pruebas:
      with self.assertRaises(utils.Error):
        reflector.encriptar(p)
        
  def test_disposicion_aleatoria(self):
    reflector = Reflector()
    self.assertIsInstance(reflector.conexiones, list)
    self.assertEqual(len(reflector.conexiones), utils.CANT_CARACTERES_ASCII)
    
    set_conexiones = set(reflector.conexiones)
    self.assertEqual(len(set_conexiones), len(reflector.conexiones))
    
    posiciones_verificadas = list()
    index = 0
    for con in reflector.conexiones:
      if posiciones_verificadas.count(index) > 0:
        continue
      self.assertNotEqual(con, index)
      self.assertEqual(reflector.conexiones[con], index)
      posiciones_verificadas.append(con)
      index += 1
      
  def test_encriptacion_invalida(self):
    reflector = Reflector()
    pruebas = ['^', 'abc', '|']
    for p in pruebas:
      with self.assertRaises(utils.Error):
        reflector.encriptar(p)
        
  def test_encriptacion(self):
    reflector = Reflector()
    caracter = random.choice(utils.CARACTERES_ASCII)
    
    resultado1 = reflector.encriptar(caracter)
    self.assertIsInstance(resultado1, str)
    self.assertEqual(len(resultado1), 1)
    
    resultado2 = reflector.encriptar(resultado1)
    self.assertIsInstance(resultado2, str)
    self.assertEqual(len(resultado2), 1)
    
    self.assertEqual(caracter, resultado2)
    
 

    
    
    
    
        
    