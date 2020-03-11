import turtle
from math import *

def ini():
	turtle.setup(600,600)
	turtle.mode("logo")
	
def pionek(size, kolor, ann):
	
	poz = size/6
	pion = poz
	skos = poz*sqrt(2)
	kat = 45
	
	
	ann.up()
	ann.fd(pion)
	ann.right(90)
	ann.fd(poz)
	ann.down()
	
	ann.fillcolor(kolor)
	ann.begin_fill()
	ann.fd(4*poz)
	ann.left(90+kat)
	ann.fd(skos)
	ann.right(kat)
	ann.fd(pion)
	ann.left(kat)
	ann.fd(skos)
	ann.left(180-2*kat)
	ann.fd(skos)
	ann.left(kat)
	ann.fd(pion)
	ann.right(kat)
	ann.fd(skos)
	ann.end_fill()
	
	ann.up()
	ann.right(45)
	ann.fd(poz)
	ann.left(90)
	ann.fd(pion)
	ann.left(180)
	ann.down()
	

ini()
ann = turtle.Turtle()
pionek(420, "pink", ann)
turtle.mainloop()