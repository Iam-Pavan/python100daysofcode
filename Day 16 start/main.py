import another_module
print(another_module.another_variable)
# import turtle
# from turtle import Turtle,Screen
# timmy = Turtle()
# print('str')
# timmy.shape('circle')
# timmy.color('red')
# timmy.forward(150)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# turtle.color('red')
from  prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','water',another_module.another_variable])
table.align = 'l'
print(table)

