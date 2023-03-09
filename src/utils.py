CARACTERES_ASCII = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú1234567890 ¿?:.;,!’"()#$%&/[]+*\'-_~<>=£@'
CANT_CARACTERES_ASCII = len(CARACTERES_ASCII)

ALFABETO_ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CANT_ALFABETO_ENG = len(ALFABETO_ENG)

def verificar_caracter(caracter: str, caracteres: str) -> bool:
  return len(caracter) == 1 and caracter in caracteres

CONEXIONES_ENG_ROTOR_1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
CONEXIONES_ENG_ROTOR_2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
CONEXIONES_ENG_ROTOR_3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
CONEXIONES_REFLECTOR_ENG = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

CONEXIONES_ROTORES_ENG = [CONEXIONES_ENG_ROTOR_3, CONEXIONES_ENG_ROTOR_2, CONEXIONES_ENG_ROTOR_1]

# for i in range(0, CANT_ALFABETO_ENG):
#   char = ALFABETO_ENG[i]
#   enc = ALFABETO_ENG[CONEXIONES_ENG_ROTOR_3[i]]
#   print(f'{i}. {char} -> {enc}')

class Error(Exception):
  pass
