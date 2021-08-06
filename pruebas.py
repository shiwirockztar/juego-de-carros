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
	rivals=[]
     

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

	def rival(self,r):
		self.rivals.append(r)
		print(self.rivals)
		pass


players=random.randint(2, 6) 
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
	# 
	xa=random.choice(newCnd)
	rivals.append(xa)
	# print("el jugador ",i+1,"juega con ",xa,"que lleva el carro ", end='')
	xb=random.choice(newcars)
	rivals.append(xb)
	# print(xb," y le fue asignado el carril ", i+1)
	newCnd = [w for w in newCnd if xa != w]
	# print(newCnd, "  ",xa)
	newcars = [w for w in newcars if xb != w]
	# print(newcars, "  ",xb)
	a.rival(rivals)
	i+=1
	pass

print(rivals)
# a.rival(rivals)
# a.copiar()

time.sleep(5)    
print(" ")

os.system('pause')




