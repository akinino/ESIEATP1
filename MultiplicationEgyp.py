def Egypt(x,y):
	resultat = 0

	while(y > 0):
		if(y % 2 == 0):
			x += x
			y /= 2
		else:
			resultat += x
			y -= 1
	print("Le resultat est = ",resultat)

x = int(input("Donnez la valeur de x = "))
y = int(input("Donnez la valeur de y = "))
Egypt(x,y)
