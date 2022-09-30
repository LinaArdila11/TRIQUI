from Tablero import Tablero
from Jugador import Jugador

class Juego:

    def __init__(self):

        #Primer jugador 
        self.miJugador=Jugador("humano")

        #Segundo jugador
        self.computador=Jugador("computador")
        self.miTablero=Tablero()


    def jugar_triqui(self):

        self.miJugador.seleccionar_simbolo()

        if self.miJugador.miFicha.simbolo=='X':
            self.computador.miFicha.simbolo=='O'
        else:
            self.computador.miFicha.simbolo=='X'

miJuego=Juego()

