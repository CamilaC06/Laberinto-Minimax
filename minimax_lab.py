#Juego de laberinto del gato y el raton
import random
import time

#creamos el tablero
tablero = [["." for _ in range (5)]for _ in range (5)]

#función para mostrar el tablero
def mostrar(tablero):
    for fila in tablero:
        print("    ".join(fila))

# colocar un objeto en una posición
    #Definir posición inicial del gato y ratón
def poner(tablero, pos, figura):
    x, y = pos
    tablero[x][y] = figura

pos_gato = 0, 0
pos_raton = 4, 4

#Buscar los espacios por donde se puede mover
def espacio_libre():
    espacios = []
    for i, fila  in enumerate(tablero):
        for j, lugar in enumerate(fila):
            if lugar == ".":
                espacios.append((i, j))
    return espacios

#funcion para verificar movimientos posibles del jugador
def movimientos_posibles(pos):
    x, y = pos
    movs = []
    if x > 0: movs.append((x-1, y)) #espacio arriba
    if x < 4: movs.append((x+1, y)) #espacio abajo
    if y > 0: movs.append((x, y-1)) #espacio a la izquierda
    if y < 4: movs.append((x, y+1)) #espacio a la derecha
    return movs

poner(tablero, pos_raton, "🐭")
poner(tablero, pos_gato, "😼")

casilla = espacio_libre()

#Ubicar varios quesos en posiciones aleatorias y mostrar
quesos = random.sample(casilla, 3)
for qx,qy in quesos:
    tablero[qx][qy] = "🧀"

#función para mover las figuras 
def mover(tablero, pos_actual, pos_nueva, figura, quesos):
    x, y = pos_actual
    if (x, y) not in quesos:
        tablero[x][y] = "."
    ax, ay = pos_nueva
    tablero[ax][ay] = figura
    return (ax, ay)

def minimax_gato(pos_raton, movs):
    mejor_mov = movs[0]
    menor_dist = float('inf')
    for m in movs:
        dist = abs(m[0] - pos_raton[0]) + abs(m[1] - pos_raton[1])
        if dist < menor_dist:
            menor_dist = dist
            mejor_mov = m
    return mejor_mov

def minimax_raton(movs, quesos):
    mejor_mov = movs[0]
    menor_dist = float('inf')
    for m in movs:
        for q in quesos:
            dist = abs(m[0] - q[0]) + abs(m[1] - q[1])
            if dist < menor_dist:
                menor_dist = dist
                mejor_mov = m
    return mejor_mov

cant_quesos = 0
turnos = 0

#Bucle principal
while True:
    casilla = espacio_libre()
    turnos += 1
    print(f"turno nro: {turnos}")
        
    #mover a los personajes de a un paso
    mov_r = movimientos_posibles(pos_raton)
    if cant_quesos < 1:
        pos_raton = mover(tablero, pos_raton, (random.choice(mov_r)), "🐭", quesos)
    else:
        mejor_r = minimax_raton(mov_r, quesos)
        pos_raton = mover(tablero, pos_raton, mejor_r, "🐭", quesos)
    mostrar(tablero)
    print()
    time.sleep(0.5)
    
    mov_g = movimientos_posibles(pos_gato)   
    if turnos < 6: #gato aleatorio
        pos_gato = mover(tablero, pos_gato, (random.choice(mov_g)), "😼", quesos)
        
    else: #gato inteligente
        mejor_g = minimax_gato(pos_raton, mov_g)
        pos_gato = mover(tablero, pos_gato, mejor_g, "😼", quesos)
        
    
    #Si el ratón come el queso
    if pos_raton in quesos:
        cant_quesos += 1
        print(f"El ratón se ha comido {cant_quesos} queso/s ")
        quesos.remove(pos_raton)

    for qx, qy in quesos:
        if (qx, qy) != pos_raton and (qx, qy) != pos_gato:
            tablero[qx][qy] = "🧀"
        
    mostrar(tablero)
    print()
    time.sleep(0.5)
    
    
    #Condición para cuándo termina el juego
    if pos_raton == pos_gato:
        print("El juego ha terminado! El gato atrapó al ratón")
        break

    elif cant_quesos >= 3:
        print("El ratón ha ganado!")
        break
    
#Mostrar la cantidad de turnoss
print(f"Se han jugado {turnos} turnos")