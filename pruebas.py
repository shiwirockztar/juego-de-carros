import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')



class Jugadores:
	conductor=0
	carro=0 
	carril=0
	distancia=0

	tramos=[]
	podio=[]
	rivals=[]
	npista=[]
     
# constructor que inicializa los carriles que jugaran en 0
	def __init__(self,a,b,c,pl):
		# tarea agregar validaciones
		self.conductor=c
		self.carro=b
		self.carril=a
		for x in range(pl):
			self.tramos.append(0)
			pass

# mostrar nos muestra el conductor carro y posicion de carril que jugara, ademas las guarda esas posiciones en npista
	def mostrar(self,pl):
		print("El jugador juega con ",self.conductor," lleva el carro ",self.carro,"y le fue asignado el carril ",self.carril)
		self.npista.append(self.carril)
		i=0
		n=0
		k=1
		while i<pl-1:
			if k==self.carril:
				k+=1
				pass
			print(self.rivals[n]," lleva el carro ",self.rivals[n+1],"y le fue asignado el carril ",k)
			self.npista.append(k)
			i+=1
			k+=1
			n+=2
			pass
		# print(self.npista)
		# print(self.rivals)
		pass

# nos enlaza los rivales con sus carros
	def rival(self,ra,rb):
		self.rivals.append(ra)
		self.rivals.append(rb)
		# print(self.rivals)
		pass

	def competir(self,players):
		while min(self.tramos) < pista:
		# while max(self.tramos) < 10:

			# aqi en vez de x deberia ser el turno de el citado
			n=1
			i=0
			for x in range(players): 
				while i<players:
					if n==self.npista[i]:
						self.tramos[i]+=random.randint(0, 6)
						pass
					i+=1
					pass
				n+=1
				i=0
				pass
			pass
			# print(self.tramos)
			os.system('cls')
			# aqui pasamos la primera vuelta o primer
			print("la pista mide ",pista*100,"  ")
			self.Visual(players,pista)
			# os.system('cls')
			# os.system('pause')
			time.sleep(0.5)  
		pass

	def Visual(self,pl,pista):
		# print("la pista mide ",pista*100,"  ")

		i=0
		n=1
		d=0
		for x in range(pl):
			while i<pl:
				if n==self.npista[i]:
					# print(self.tramos[i]*100," Mts")
					if n==self.carril:
						print(self.conductor,"  PLAYER ",self.tramos[i]*100," Mts")
						if self.tramos[i]>pista:
							self.podio.append(self.conductor)
							pass
						pass
					elif n!=self.carril:
						# nb=(n-1)*2
						print(self.rivals[d],"         ",self.tramos[i]*100," Mts")
						if self.tramos[i]>pista:
							self.podio.append(self.rivals[d])
							pass
						d+=2	
						pass
					# print("n = ",n,"coincide con npista= ",self.npista[i])
					for w in range(self.tramos[i]):
						print("█", end='')
						pass
					print("")
					print("  __________________________\n")
					pass
				i+=1
				pass
			n+=1
			i=0
			pass
		pass
	
	def premiacion(self):
		nwpodio = []
		for x in self.podio:
			if x not in nwpodio:
				nwpodio.append(x)
				pass
			pass

		print("podio para ")
		i=0
		while i<3:
			print("lugar numero ",i+1," en el podio para",nwpodio[i])
			i+=1
			pass
		pass
	

		

players=random.randint(3, 6)
# players=2 
pista=random.randint(10, 100) 
d='y' # variable para la Desicion de aceptar mas jugadores comienza como YES


print("Bienvenido al juego de los carros\n")
print("El numero de jugadores es ",players)
print("La pista a recorrer tiene\n", pista*100,"mts")

menuC='''
         Menu :
0>montoya	 3>hamilton	 
1>vettel         4>alonzo
2>schumacher     5>speede 
'''

menuE='''
         Menu :
0>redbull	 3>BMW	 
1>lamborghini    4>sauber
2>ferrari        5>porsche 
'''

Cnd=["montoya","vettel","schumacher","hamilton","alonzo","speedy"]
cars=["redbull","lamborghini","ferrari","BMW","sauber","porsche"]

# aqui tomamos las opciones del ususario

while True:
    try:
        x = int(input("Por favor introduzca la posiciona o carril a elegir\n"))
    except ValueError:
        print("Debes escribir un número.")
        pass

    if x <= 0:
        print("Debes escribir un número positivo.")
        pass
    if x > players:
    	print("Debes escribir un carril disponible.")
    	pass

    else:
        break

print(menuE)
while True:
    try:
        y=int(input("Por favor introduzca la escuderia a elegir\n"))
    except ValueError:
        print("Debes escribir un número.")
        pass

    if y < 0:
        print("Debes escribir un número positivo.")
        pass
    if y > 5:
    	print("debes escojer una escuderia disponible.")
    	pass

    else:
        break

print(menuC)
while True:
    try:
        z=int(input("Por favor introduzca el conductor a elegir\n"))
    except ValueError:
        print("Debes escribir un número.")
        pass

    if z < 0:
        print("Debes escribir un número positivo.")
        pass
    if z > 5:
    	print("debes escojer una escuderia disponible.")
    	pass

    else:
        break



# x=2	
# y=1
# z=1

a = Jugadores(x,cars[y],Cnd[z],players)

newCnd=Cnd.copy()
newcars=cars.copy()
newCnd = [w for w in newCnd if Cnd[z] != w]
newcars = [w for w in newcars if cars[y] != w]

# /////////////////seleccionar rivales ////////////////
i=0
while i<players-1:
	# 
	xa=random.choice(newCnd)
	xb=random.choice(newcars)
	newCnd = [w for w in newCnd if xa != w]
	# print(newCnd, "  ",xa)
	newcars = [w for w in newcars if xb != w]
	# print(newcars, "  ",xb)
	a.rival(xa,xb)
	# a.rival(rivals)

	i+=1
	pass
# -----------------------------------------------------------------
a.mostrar(players)
os.system('pause')

a.competir(players)
a.premiacion()

time.sleep(5)    
print(" ")

os.system('pause')




