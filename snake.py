"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from random import randrange
from turtle import *
import random
from freegames import square, vector

food = vector(0, 0)

snake = [vector(10, 0)]
aim = vector(0, -10)
#Se agrego una lista de colores
colors = ['green','blue','yellow','orange','pink']
#elige de forma aleatoria los valores
num_al_body = random.randint(0, 4)
num_al_food = random.randint(0, 4)
#El valor esta en uso elige otro
while num_al_body == num_al_food:
    num_al_body = random.randint(0, 4)

food_limits = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]

def move_food():
    # Randomizamos el movimiento de comida
    move_direction = choice(food_limits)
    next_position = food + move_direction
    
    if inside(next_position):
        food.move(move_direction)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    #Usa el indice del valor para el color.
    for body in snake:
        square(body.x, body.y, 9, colors[num_al_body])

    square(food.x, food.y, 9, colors[num_al_food])
    update()
    
    move_food()
    
    

    ontimer(move, 100)


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
