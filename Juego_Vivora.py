#
#
# Este codigo genera una simulacion del juego Vivora, donde el objetivo es movernos con las flechas por toda la ventana comiendo
# los squares que se moveran aleatoriamente. Las formas de perder es si chocamos con nuestro mismo cuerpo o con los limites de
# la ventana de juego.

from turtle import *
import random
from random import randrange
from freegames import square, vector


food = vector(0, 0) # Posicion de inicio de la comida
snake = [vector(10, 0)] #Posicion de inicio de la serpiente
aim = vector(0, -10)

def change(x, y): # Esta funcion nos muestran los cambios de a donde se dirije ya que existe un movimiento en el eje y tanto negativo como positivo y uno en x igual positivo y negativo creando un moivimiento a arriba,abajo,izquierda, derecha
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):#Funcion que recibe las coordenadas de la cabeza y verifica que este en los limites
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190 #Limites de la ventana de juego


def changeFo(): # Esta funcion fue creada para que la comida tuviese un movimiento constante hasta que chocara con los limites y asi detenerse incrementando la dificultad del juego 
    if -150 < food.x + 10 < 150 and -150 < food.y < 150: #Este es el rango en el que la manzana se desplazara cambiando de ubicacion y sin salirse del margen 
        food.y = food.y + randrange(-1, 2) * 10 #Aqui se muestra como la manzana se mueve definiendo su movimiento cambiando esto podriamos hacer que la manza tuviese movimientos mas simples o mas extensos al punto de hacer el juego imposible o facil
        food.x = food.x + randrange(-1, 2) * 10
    elif -150 == food.x:
        food.x = food.x + 10
    elif 150 == food.x:
        food.x = food.x - 10
    elif -150 == food.y:
        food.y = food.y + 10
    elif 150 == food.y:
        food.y = food.y - 10
        

colorCom = random.choice(['green', 'yellow','blue','orange','purple']) #Dentro de este random se elegira un color para el square de la comida
colorSer = random.choice(['green', 'yellow','blue','orange','purple']) #Dentro de este random se elegira un color para el square de la serpiente

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    
    if not inside(head) or head in snake: # Si la serpiente esta fuera de los limites o toco su cuerpo...
        square(head.x, head.y, 9, 'red') # cambiara a color rojo
        update() # Actualiza el estado del cuadrado(serpiente)
        return

    snake.append(head)

    if head == food: # Cuando la cabeza de la serpiente toca la comida
        print('Snake:', len(snake)) # Imprime el valor de puntos al 'comer' 
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
  

    clear() # Borra el square comida de la pantalla


    for body in snake:
        if colorCom != colorSer: # Este if evita que los colores de la comida y la serpiente sean los mismos
            square(body.x, body.y, 9, colorSer) # Añade la propiedad del color a la serpiente
            square(food.x, food.y, 9, colorCom) # Añade la propiedad del color a la comida
        else:   # En caso de que los colores generados aleatoriamente se repitan se usaran estos por default
            square(body.x, body.y, 9, 'blue')
            square(food.x, food.y, 9, 'green')
            
    update()
    ontimer(move, 150)#Aqui esta la velocidad que tomara la serpiente ya que entre mas alto el numero su velocidad disminuye haciendo el juego mas facil que anteriormente
    ontimer(changeFo,150)#Estos timers fueron creados para que la funcion se moviese a cierta velocidad


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

    
move()
done()