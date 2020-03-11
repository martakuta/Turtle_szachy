import turtle
from math import *

def ini():
	turtle.setup(600,600)
	turtle.mode("logo")
	
def konik(size, kolor, ann):
	
	poz = size/4
	pion = size/5
	skos = sqrt(poz*poz+pion*2*pion*2)
	kat = asin(sqrt(25/89))
	kat = kat/pi *180
	
	
	ann.up()
	ann.fd(pion)
	ann.right(90)
	ann.fd(poz)
	ann.down()
	
	ann.fillcolor(kolor)
	ann.begin_fill()
	ann.fd(2*poz)
	ann.left(90)
	for i in range(4):
		ann.fd(pion/2)
		ann.left(90)
		ann.pensize(2)
		ann.fd(poz/2)
		ann.left(180)
		ann.fd(poz/2)
		ann.pensize(1)
		ann.left(90)
	ann.fd(pion)
	ann.left(90)
	ann.fd(poz*3/4)
	ann.left(90)
	ann.up()
	ann.fd(pion/2)
	ann.down()
	ann.dot(pion/4, "black")
	ann.left(180)
	ann.up()
	ann.fd(pion/2)
	ann.down()
	ann.left(90)
	ann.fd(poz*5/4)
	ann.left(90)
	ann.fd(pion/2)
	ann.left(90)
	ann.pensize(2)
	ann.fd(poz/2)
	ann.left(180)
	ann.fd(poz/2)
	ann.pensize(1)
	ann.left(90)
	ann.fd(pion/2)
	ann.left(90)
	ann.fd(poz)
	ann.right(90+kat)
	ann.fd(skos)
	ann.end_fill()
	
	ann.up()
	ann.right(90-kat)
	ann.fd(poz)
	ann.left(90)
	ann.fd(pion)
	ann.left(180)
	ann.down()
	

ini()
ann = turtle.Turtle()
konik(420, "pink", ann)
turtle.mainloop()