tab_fila1 = ["-","-","-"]
tab_fila2 = ["-","-","-"]
tab_fila3 = ["-","-","-"]

def imprimir_tablero_numerado():
    print("1  2  3\n4  5  6\n7  8  9\n")

def imprimir_tablero_juego():
    for p in tab_fila1:
        print ('|'+p, end='')
    print('|', end='')
    print("")
    for p in tab_fila2:
        print ('|'+p, end='')
    print('|', end='')
    print("")
    for p in tab_fila3:
        print ('|'+p, end='')
    print('|', end='')
    print("")

def leer_posicion():
    posicion=""
    posicion = input("Seleccione posicion (1-9):")
    return posicion

def ubicar_en_tablero(una_posicion, un_simbolo):
    if (una_posicion=='1'):
        tab_fila1[0]=un_simbolo
    if (una_posicion=='2'):
        tab_fila1[1]=un_simbolo
    if (una_posicion=='3'):
        tab_fila1[2]=un_simbolo
    if(una_posicion=='4'):
        tab_fila2[0]=un_simbolo
    if(una_posicion=='5'):
        tab_fila2[1]=un_simbolo
    if(una_posicion=='6'):
        tab_fila2[2]=un_simbolo
    if(una_posicion=='7'):
        tab_fila3[0]=un_simbolo
    if(una_posicion=='8'):
        tab_fila3[1]=un_simbolo
    if(una_posicion=='9'):
        tab_fila3[2]=un_simbolo


def pedir_movimiento(un_numero_de_jugador):
    print("Turno Jugador {}".format(un_numero_de_jugador))
    print("Tablero de juego:")
    imprimir_tablero_juego()
    # print("Elija movimiento: ")
    posi_elegida = leer_posicion()
    return posi_elegida


def hay_ganador():
    hay = False

    return hay



if __name__ == "__main__":
    turno_player_1 = True
    print ("BIENVENIDO")

    while(hay_ganador()==False):
        #turno player 1
        if (turno_player_1):
            pos = pedir_movimiento(1)
            ubicar_en_tablero(pos,'X')
            imprimir_tablero_juego()
            imprimir_tablero_numerado()
            turno_player_1 = False      #fin del turno
        
        #turno player 2
        else:
            pedir_movimiento(2)
            pos = pedir_movimiento(2)
            ubicar_en_tablero(pos,'O')
            imprimir_tablero_juego()
            imprimir_tablero_numerado()
            turno_player_1 = True       #fin del turno
