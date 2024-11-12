import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")
color("#f73487")
penup()
goto(0, -100)
pendown()

# Draw the heart shape
for i in range(600):
    goto(hearta(i) * 20, heartb(i) * 20)
    dot(2)

# Add "I love you Mona🫀" text in the center
penup()
goto(-70, 50)  # Adjust position as needed
color("white")
write("I love you, Mona", align="center", font=("Arial", 24, "bold"))

done()

