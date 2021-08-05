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
	tramos=[]
     

	def __init__(self,a,b,c):
		self.conductor=a
		self.carro=b
		self.carril=c

	def mostrar(self,x):
		print("El jugador ",x," juega con ",self.Cnd[self.conductor],"que lleva el carro ",self.cars[self.carro],"y le fue asignado el carril ",self.carril)

	def correr(self,x,y):
		# en esta parte podemos agregar un atraso o un avanze si el ejercicio lo amerita
		self.tramos[y]+=x

	def copiar(self):
		self.k.append(self.Cnd[self.conductor])
		self.k.append(self.cars[self.carro])
		self.k.append(self.carril)
		self.tramos.append(0)


	def Histori(self):
		print(self.k)
          
	def Visual(self,pl):
		# para cada jugador
		for x in range(pl):
			
			# imprime numero de distancia equivalentes a 100 mts
			print(self.Cnd[x],"  ",self.tramos[x],"00 mts"  )
			for Mts in range(self.tramos[x]):
				print("█", end='')
				pass
			print("")
			print("  __________________________\n")
			pass
			
	def premiacion(self):
		
		print(self.k)

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
    
print(" ")

# primera vuelta

for y in range(players):

	dxpl=random.randint(0, 6) #dado
	# print("el valor de rrecorrido por el jugador ",y," fue ",dxpl)
	a.correr(dxpl,y)
	time.sleep(1)

# premiacion



# print("aqui viene el histori\n")
# a.Histori()
a.Visual(players)
time.sleep(10)
# os.system('cls')
os.system('pause')

