import sys
import os

path = os.path.abspath('gui/')
sys.path.append(path)

from principal import VentanaPrincipal

def main():
  ventana1 = VentanaPrincipal()
  ventana1.show()
    
main()

