# Laberinto-Minimax

Juego del laberinto del gato y el ratón 
Autor: Camila Cabriza 
Lenguaje: Python
Estado: funcionando

# ¿Qué es?
Se trata de un juego de dos jugadores, el gato y el ratón, que se encuentran en un laberinto (representado por un tablero de 5x5) donde deben moverse de a un paso, para lograr su objetivo y ganar el juego. 
# ¿Cómo funciona?
Durante este juego, el gato buscará atrapar al ratón, así que, al inicio se moverá de manera aleatoria, y luego de cierta cantidad de turnos, evolucionará para calcular el movimiento que más lo acerque al ratón. Por otro lado, el ratón buscará comerse los quesos del tablero, también se moverá de manera aleatoria hasta que se encuentre con un queso, a partir de ahí, calculará sus movimientos para llegar a los siguientes quesos más rápido.
# ¿Cómo se determina el ganador?
Para el gato: Este irá detrás del ratón, si lo atrapa, es el ganador
Para el ratón: Buscará los quesos, y cuando haya comido tres de ellos, será el ganador.
Una vez que uno de los personajes gana, el juego termina. No tiene un límite de turnos, por lo tanto, se seguirá jugando hasta que haya un ganador.
# ¿Qué herramientas utiliza?
+ Listas
+ Funciones
+ Algoritmo Minimax simplificado (sin recursividad completa, usado como heurística)
+ Bucle While (bucle principal del juego)
+ Condicionales if, else (para determinar el ganador)
+ Librerías: random y time
+ Representación visual: emojis en la consola y “.” para los espacios vacíos
# ¿Cómo ejecutarlo?
Ejecutar Visual Studio Code, abrir el archivo, ir a la terminal y escribir: “python minimax_lab.py” para ejecutarlo.
