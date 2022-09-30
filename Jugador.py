import random
from Ficha import Ficha

class Jugador:

    def __init__ (self,valor):

        self.miFicha=Ficha ()
        self.tipo=valor

    def realizar_jugada(self,untablero):

        x=-1
        y=0

        while untablero.verificarJugada(x,y)==False:

            if self.tipo=="humano":
                 x=int(input("Ingrese una fila:"))
                 y=int(input("Ingrese una columna:"))
            else:

                x=random.randint(0,2)
                y=random.randint(0,2)


        untablero.matriz[x][y]= self.miFicha.simbolo
        return untablero

    def seleccionar_simbolo (self):

        x=random.randint(0,1)
        if x==0:
            self.miFicha.simbolo='O'
        else:
            self.miFicha.simbolo='X'