import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')



class Jugadores:
	# conductor=0
	# carro=0 
	# carril=0
	distancia=0
	Cnd=["montoya","vettel","schumacher","hamilton","alonzo","speede"]
	cars=["redbull","lamborghini","ferrari","BMW","sauber","porsche"]
	k=[]
     

	def __init__(self,a,b,c):
		self.conductor=a
		self.carro=b
		self.carril=c

	def mostrar(self,x):
		print("El jugador ",x," juega con ",self.Cnd[self.conductor],"que lleva el carro ",self.cars[self.carro],"y le fue asignado el carril ",self.carril)

	def correr(self,x,y):
		# en esta parte podemos agregar un atraso o un avanze si el ejercicio lo amerita
		self.k[y]+=x

	def copiar(self):
		self.k.append(self.Cnd[self.conductor])
		self.k.append(self.cars[self.carro])
		self.k.append(self.carril)
		self.k.append(0)

	def Histori(self):
		print(self.k)
          
	def Visual(self,pl):
		# para cada jugador
		for x in range(pl):
			print(self.Cnd[x] )
			# imprime numero de distancia equivalentes a 100 mts
			if x==0:
				y=3
				pass
			if x==1:
				y=7
				pass
			if x==2:
				y=11
				pass
			if x==3:
				y=15
				pass
			if x==4:
				y=19
				pass
			if x==5:
				y=23
				pass
			if x==6:
				y=27
				pass
			for Mts in range(self.k[y]):
				print("█", end='')
				pass
			print("")
			print("  __________________________\n")
			pass
			

pista=random.randint(10, 100) 
d='y' # variable para la Desicion de aceptar mas jugadores comienza como YES
print("Bienvenido al juego de los carros\n")

print("La pista a recorrer tiene\n", pista*100,"mts")
time.sleep(1)
players=random.randint(2, 6) 
print("El numero de autos compitiendo son\n", players,"autos")


# x comienza en el numero 0
for x in range(players):

    a = Jugadores(x,x,x)
    a.mostrar(x+1)
    a.copiar()
    

# primera vuelta
for y in range(players):

	if y==0:
		despl=3
		pass
	if y==1:
		despl=7
		pass
	if y==2:
		despl=11
		pass
	if y==3:
		despl=15
		pass
	if y==4:
		despl=19
		pass
	if y==5:
		despl=23
		pass
	if y==6:
		despl=27
		pass
	dxpl=random.randint(0, 6) #dado
	# print("el valor de rrecorrido por el jugador ",y," fue ",dxpl)
	a.correr(dxpl,despl)





# print("aqui viene el histori\n")
# a.Histori()
a.Visual(players)
time.sleep(10)
# os.system('cls')
os.system('pause')

