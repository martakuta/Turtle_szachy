#Marta Markocka
#WdI, zadanie domowe nr 4

import turtle
from math import *

def ini(ann):
	turtle.setup(1000,1000)
	turtle.mode("logo")
	ann.speed(100)


def goniec(size, kolor, ann):
	#rysuje szachowa figure gonca wedlug zadanego schematu

	poz = size/6
	pion = size/7
	skos = sqrt(poz*poz+pion*pion) #dlugosc skosnych linii
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

def wieza(size, kolor, ann):
	#rysuje szachowa figure wiezy wedlug zadanego schematu

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

def hetman(size, kolor, ann):
	#rysuje szachowa figure hetmana wedlug zadanego schematu

	poz = size/8
	pion = size/6
	skos = sqrt(poz*poz+pion*pion) #dlugosc skosnych linii
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

def pionek(size, kolor, ann):
	#rysuje szachowa figure pionka wedlug zadanego schematu

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

def konik(size, kolor, ann):
	#rysuje szachowa figure konika wedlug zadanego schematu
	
	poz = size/4
	pion = size/5
	skos = sqrt(poz*poz+pion*2*pion*2) #dlugosc linii skosnej
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

def krol(size, kolor, ann):
	#rysuje szachowa figure krola wedlug zadanego schematu
	
	poz = size/6
	pion = size/6

	ann.up()
	ann.fd(pion)
	ann.right(90)
	ann.fd(2*poz)
	ann.down()

	ann.fillcolor(kolor)
	ann.begin_fill()
	ann.fd(2*poz)
	ann.left(90)
	ann.fd(pion)
	ann.fd(pion)
	ann.left(90)
	ann.fd(2*poz)
	ann.left(90)
	ann.fd(pion)
	ann.fd(pion)
	ann.left(90)
	ann.end_fill()

	ann.begin_fill()
	ann.left(90)
	ann.fd(pion)
	ann.right(90)
	ann.circle(pion)
	ann.up()
	ann.fd(2*poz)
	ann.down()
	ann.circle(pion)
	ann.end_fill()

	ann.up()
	ann.left(90)
	ann.fd(2*pion)
	ann.left(90)
	ann.fd(5/6*poz)
	ann.right(90)
	ann.down()
	ann.begin_fill()
	ann.fd(3/2*pion)
	ann.left(90)
	ann.fd(1/3*poz)
	ann.left(90)
	ann.fd(3/2*pion)
	ann.left(90)
	ann.fd(1/3*poz)
	ann.end_fill()
	ann.up()
	ann.right(90)
	ann.fd(pion/2)
	ann.right(90)
	ann.fd(1/6*pion)
	ann.left(180)
	ann.down()
	ann.begin_fill()
	ann.circle(pion/2)
	ann.end_fill()

	ann.up()
	ann.right(90)
	ann.fd(7/2*pion)
	ann.right(90)
	ann.fd(3*poz)
	ann.right(90)
	ann.down()


def plansza(size, wiersze, kolumny, uklad, kolor_gracza_1,
			kolor_gracza_2, kolor_planszy_1, kolor_planszy_2, ann):
	#rysuje pojedyncza plansze wedlug zadanych parametrow

	indeks = 0 #czyli ktore z kolei pole jest rysowane
	for w in range(wiersze):
		for k in range(kolumny):

			if w%2 == k%2: 	#w parzystych wierszach pola z parzystych kolumn sa w kolorze 1
							#w nieparzystych wierszach w kolorze 1 sa pola z kolumn nieparzystych
				ann.fillcolor(kolor_planszy_1)
			else:
							#pozostale pola sa w kolorze 2
				ann.fillcolor(kolor_planszy_2)
			
			#rysuje zamalowany obszar pola szachownicy
			ann.begin_fill()
			for i in range(4):
				ann.fd(size)
				ann.right(90)
			ann.end_fill()

			#rysuje jesli tak wskazuje "uklad"  odpowiednia figure szachowa na danym polu
			#funkcja ord('x') zwraca kod ASCII znaku
			if ord(uklad[indeks]) >= ord('A') and ord(uklad[indeks]) <= ord('Z'):
				if (uklad[indeks] == 'P'):
					pionek(size, kolor_gracza_2, ann)
				elif (uklad[indeks] == 'R'):
					wieza(size, kolor_gracza_2, ann)
				elif (uklad[indeks] == 'N'):
					konik(size, kolor_gracza_2, ann)
				elif (uklad[indeks] == 'B'):
					goniec(size, kolor_gracza_2, ann)
				elif (uklad[indeks] == 'K'):
					krol(size, kolor_gracza_2, ann)
				elif (uklad[indeks] == 'Q'):
					hetman(size, kolor_gracza_2, ann)

			elif ord(uklad[indeks]) >= ord('a') and ord(uklad[indeks]) <= ord('z'):
				if (uklad[indeks] == 'p'):
					pionek(size, kolor_gracza_1, ann)
				elif (uklad[indeks] == 'r'):
					wieza(size, kolor_gracza_1, ann)
				elif (uklad[indeks] == 'n'):
					konik(size, kolor_gracza_1, ann)
				elif (uklad[indeks] == 'b'):
					goniec(size, kolor_gracza_1, ann)
				elif (uklad[indeks] == 'k'):
					krol(size, kolor_gracza_1, ann)
				elif (uklad[indeks] == 'q'):
					hetman(size, kolor_gracza_1, ann)

			#przesuwam indeks i przechodze do startu nastepnego pola
			indeks += 1
			if k < kolumny-1:
				ann.up()
				ann.right(90)
				ann.fd(size)
				ann.left(90)
				ann.down()
			else:
				ann.up()
				ann.fd(size)
				ann.left(90)
				ann.fd((kolumny-1)*size)
				ann.right(90)
				ann.down()

def rysunek(ann):
	#rysuje caly rysunek skladajacy sie z siedmiu planszy

	p0 = "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"  # układ startowy
	p1 = "r.b.kb.rpppp.pp...n..q.p....p......P......P.....PP..PPPPRNBQKBNR"  # obrona Caro-Kann, atak dwu skoczków
	p2 = "rnbqk..rpppp.ppp.....n......p....b..P.....N.....PPPP.PPPR.BQKBNR"  # partia hiszpańska
	p3 = "rnbqkbnrpp..pppp..........pp.......P............PPP.PPPPRNBQKBNR"  # gambit hetmański
	p4 = "r....r.k.b..q..pp.n...p..p..bpNQ.P..p...PB..P....B...PPP..RR..K."  # nieśmiertelna partia Rubinsteina z 1907, Akiba Rubinstein (czarne), najsłynniejszy polski szachista wszechczasów
	p5 = "rnbqkppppp.....PPPPPRNBQK"  # plansza 5 * 5
	p6 = "rqkrpppp....PPPPRQKR"  # plansza 5 * 4

	#wszystkie ruchy zolwia ponizej sa wywolywane z "ann." na poczatku
	#mimo ze na moodle jest bez nich ale inaczej nie kompilowalo sie u mnie na komputerze
	
	ann.up();ann.goto(-310,150);ann.down()
	ann.lt(45)
	plansza(25, 8, 8, p0, "orange", "green", "gold", "yellow", ann)

	ann.up();ann.goto(-170,-290);ann.down()
	ann.lt(90)
	plansza(25, 8, 8, p1, "cyan", "DarkRed", "gold", "yellow", ann)

	ann.up();ann.goto(300,-140);ann.down()
	ann.lt(90)
	plansza(25, 8, 8, p2, "aqua", "chartreuse", "DarkKhaki", "yellow", ann)

	ann.up();ann.goto(170,290);ann.down()
	ann.lt(90)
	plansza(25, 8, 8, p3, "purple", "cornflower blue", "silver", "yellow", ann)

	ann.up();ann.goto(-160,-160);ann.down()
	ann.lt(45)
	plansza(40, 8, 8, p4, "beige", "brown", "silver", "white", ann)

	ann.up();ann.goto(-50,250);ann.down()
	plansza(20, 5, 5, p5, "light goldenrod yellow", "dark salmon", "DarkKhaki", "yellow", ann)

	ann.up();ann.goto(-50,-330);ann.down()
	plansza(20, 5, 4, p6, "crimson", "green", "silver", "lemon chiffon", ann)

	ann.up();ann.goto(0,0);ann.down()
	ann.lt(45)

#inicjalizacja zolwika i zalozen ogolnych
ann = turtle.Turtle()
ini(ann)

#jako parametr do wszystkich funkcji przekazuje zolwia "ann", aby funkcja rozpoczynala
#swoje dzialanie tam gdzie ostatnio zolw je zakonczyl
rysunek(ann)

#czeka az uzytkownik zamknie okno z rysunkiem
turtle.mainloop()