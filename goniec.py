import turtle
from math import *

def ini():
	turtle.setup(600,600)
	turtle.mode("logo")
	
def goniec(size, kolor, ann):
	
	poz = size/6
	pion = size/7
	skos = sqrt(poz*poz+pion*pion)
	kat = asin(sqrt(49/85))
	kat = kat/pi *180
	
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
	ann.fd(3*pion)
	ann.left(kat)
	ann.fd(skos)
	ann.left(180-2*kat)
	ann.fd(skos)
	ann.left(kat)
	ann.fd(3*pion)
	ann.right(kat)
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
goniec(420, "pink", ann)
turtle.mainloop()