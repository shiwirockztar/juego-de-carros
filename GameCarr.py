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
	podio=[]
     

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
		newlist=self.tramos.copy()
		for x in range(3):

			# self.tramos.index(max(newlist))->el maximo tramo de todos los jugadores
			if self.tramos.count(self.tramos[self.tramos.index(max(newlist))])>=2:
				print("Hay empate entre",self.Cnd[self.tramos.index(max(newlist))] ,"y ",self.Cnd[self.tramos.index(max(newlist),self.tramos.index(max(newlist))+1)])
				pass

			if self.tramos.count(self.tramos[self.tramos.index(max(newlist))])<2:
				print(self.Cnd[self.tramos.index(max(newlist))])
				pass
			# print(self.tramos.index(max(newlist)))
			newlist = [x for x in newlist if x != newlist[newlist.index(max(newlist))]]

	def ciclos(self,pista,players):
		while max(self.tramos) < pista:

			# print(max(self.tramos))
			for x in range(players):
				self.tramos[x]+=random.randint(0, 6)
				pass
			
			pass
			# print(self.tramos)


		

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
time.sleep(5)    
print(" ")

a.ciclos(pista,players)

# print("aqui viene el histori\n")
# a.Histori()
a.Visual(players)
a.premiacion()

time.sleep(10)
# os.system('cls')
os.system('pause')

-----------------------------------------------------------------------------------------------------------------------
elementos a actualizar y hacer cambios

import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')



class Jugadores:
	conductor=0
	carro=0 
	carril=0
	distancia=0
	# Cnd=["montoya","vettel","schumacher","hamilton","alonzo","speede"]
	# cars=["redbull","lamborghini","ferrari","BMW","sauber","porsche"]
	k=[]
	tramos=[]
	podio=[]
     

	def __init__(self,a,b,c):
		self.conductor=c
		self.carro=b
		self.carril=a

	def mostrar(self):
		print("El jugador juega con ",self.conductor,"que lleva el carro ",self.carro,"y le fue asignado el carril ",self.carril)

	def copiar(self):
		self.k.append(self.conductor)
		self.k.append(self.carro)
		self.k.append(self.carril)
		self.tramos.append(0)
		pass


players=random.randint(2, 6) 
pista=random.randint(10, 100) 
d='y' # variable para la Desicion de aceptar mas jugadores comienza como YES


print("Bienvenido al juego de los carros\n")
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

Cnd=["montoya","vettel","schumacher","hamilton","alonzo","speede"]
cars=["redbull","lamborghini","ferrari","BMW","sauber","porsche"]
rivals=[]


# aqui tomamos las opciones del ususario

x=int(input("Por favor introduzca la posiciona o carril a elegir\n"))
print(menuE)
y=int(input("Por favor introduzca la escuderia a elegir\n"))
print(menuC)
z=int(input("Por favor introduzca el conductor a elegir\n"))

a = Jugadores(x,cars[y],Cnd[z])
a.mostrar()

newCnd=Cnd.copy()
newcars=cars.copy()
newCnd = [w for w in newCnd if Cnd[z] != w]
newcars = [w for w in newcars if cars[y] != w]
# print(newCnd)
# print(newcars)

i=0
while i<players-1:
	xa=random.choice(newCnd)
	rivals.append(xa)
	print("el jugador ",i+1,"juega con ",)
	xb=random.choice(newcars)
	rivals.append(xb)

	i+=1
	pass

print(rivals)
a.copiar()

time.sleep(5)    
print(" ")

os.system('pause')