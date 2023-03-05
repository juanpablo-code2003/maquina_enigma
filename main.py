from src.enigma import Config, enigma
import src.utils as utils

def main():
  try:
    configuracion = Config(
      aleatorio=False,
      cadena_inicial='AZY',
      cadena_caracteres_vuelta_completa='ZZZ',
      caracteres_permitidos=utils.ALFABETO_ENG
    )
    mensaje = 'MENSAJE'
    encriptado = enigma(config=configuracion, msg=mensaje)
    print(f'Mensaje: {mensaje}')
    print(f'Encriptado: {encriptado}')
    print(f'Desencriptado: {enigma(config=configuracion, msg=encriptado)}')
  except utils.Error as err:
    print(err)
    
main()