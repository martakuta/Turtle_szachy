import turtle
from math import *

def ini():
	turtle.setup(600,600)
	turtle.mode("logo")
	
def hetman(size, kolor, ann):
	
	poz = size/8
	pion = size/6
	skos = sqrt(poz*poz+pion*pion)
	kat = asin(sqrt(36/100))
	kat = kat/pi *180
	
	
	ann.up()
	ann.fd(pion)
	ann.right(90)
	ann.fd(poz)
	ann.down()
	
	ann.fillcolor(kolor)
	ann.begin_fill()
	ann.fd(6*poz)
	ann.left(90)
	ann.fd(3*pion)
	for i in range(3):
		ann.up()
		ann.fd(pion/4)
		ann.right(90)
		ann.down()
		ann.circle(pion/4)
		ann.right(90)
		ann.up()
		ann.fd(pion/4)
		ann.down()
		ann.right(kat)
		ann.fd(skos)
		ann.right(180-2*kat)
		ann.fd(skos)
		ann.right(kat)
	ann.up()
	ann.fd(pion/4)
	ann.right(90)
	ann.down()
	ann.circle(pion/4)
	ann.right(90)
	ann.up()
	ann.fd(pion/4)
	ann.down()
	ann.fd(3*pion)
	ann.end_fill()
	
	ann.up()
	ann.fd(pion)
	ann.right(90)
	ann.fd(poz)
	ann.right(90)
	ann.down()
	

ini()
ann = turtle.Turtle()
hetman(420, "pink", ann)
turtle.mainloop()