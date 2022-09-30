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
            self.computador.miFicha.simbolo='O'
        else:
            self.computador.miFicha.simbolo='X'

        jugadas=0

        while Jugador<9:
            self.miJugador.realizar_jugada(self.miTablero)
            if self.miTablero.verificar_triqui():
                print("GANADOR")
                return True
            self.computador.realizar_jugada(self.miTablero)
            if self.miTablero.verificar_jugada():
                print("PERDEDOR")
                return True

            jugadas=jugadas+1

miJuego=Juego()
miJuego.jugar_triqui()
