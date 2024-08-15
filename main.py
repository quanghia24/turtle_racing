import turtle
import time
import random

WIDTH, HEIGHT = 800, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown']

def get_number_of_turtles():
    while (True):
        number = input('How many turtles do you want to race?(2-10) ')
        if(number.isdigit()):
            number = int(number)
        else:
            print('Pls enter a number!')
            continue
        if (2 <= number <= 10):
            return number
        print("Number is not in range provided")

def init_turtle():    
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing")


def create_racer(colors):
    turtles = []
    spacing = (WIDTH)//(len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # set pos
        racer.setpos((i+1)*spacing - WIDTH/2, -HEIGHT//2 + 30)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_racer(colors)
    run = True
    while (run):
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            if (y >= HEIGHT//2 - 10):
                run = False
    maxV = 0
    for i, turtle in enumerate(turtles):
        x, y = turtle.pos()
        if (y > maxV):
            maxV = y
            ans = colors[i] 
    return ans
def main():
    racers = get_number_of_turtles()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    print("The winner is", winner)

main()
