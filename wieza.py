import turtle
from math import *

def ini():
	turtle.setup(600,600)
	turtle.mode("logo")
	
def wieza(size, kolor, ann):
	
	poz = size/7
	pion = size/6	
	
	ann.up()
	ann.fd(pion)
	ann.right(90)
	ann.fd(2*poz)
	ann.down()
	
	ann.fillcolor(kolor)
	ann.begin_fill()
	ann.fd(3*poz)
	ann.left(90)
	ann.fd(2*pion)
	ann.right(90)
	ann.fd(poz)
	ann.left(90)
	ann.fd(pion)
	for i in range(2):
		ann.fd(pion)
		ann.left(90)
		ann.fd(poz)
		ann.left(90)
		ann.fd(pion)
		ann.right(90)
		ann.fd(poz)
		ann.right(90)
	ann.fd(pion)
	ann.left(90)
	ann.fd(poz)
	ann.left(90)
	ann.fd(2*pion)
	ann.left(90)
	ann.fd(poz)
	ann.right(90)
	ann.fd(2*pion)
	ann.end_fill()
	
	ann.up()
	ann.fd(pion)
	ann.right(90)
	ann.fd(2*poz)
	ann.right(90)
	ann.down()
	
	

ini()
ann = turtle.Turtle()
wieza(420, "pink", ann)
turtle.mainloop()