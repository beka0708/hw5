from classs import Hero

hero = Hero('beka', 'fly')

from classs import Hero_super

sup = Hero_super('Arlen', 'run')

print(sup.name_hero())
print(sup.__str__())

from turtle import *
color("#a7ff3d")
bgcolor("black")
speed(11)
hideturtle()
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
end_fill()
done()