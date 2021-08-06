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

	def mostrar(self,pl):
		print("El jugador juega con ",self.conductor," lleva el carro ",self.carro,"y le fue asignado el carril ",self.carril)
		i=0
		n=0
		k=1
		while i<pl-1:
			if k==self.carril:
				k+=1
				pass
			print("El jugador juega con ",self.rivals[n]," lleva el carro ",self.rivals[n+1],"y le fue asignado el carril ",k)
			i+=1
			k+=1
			n+=2
			pass
		pass

	def copiar(self):
		self.k.append(self.conductor)
		self.k.append(self.carro)
		self.k.append(self.carril)
		self.tramos.append(0)
		pass

	def rival(self,ra,rb):
		self.rivals.append(ra)
		self.rivals.append(rb)
		# print(self.rivals)
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

# aqui tomamos las opciones del ususario

# x=int(input("Por favor introduzca la posiciona o carril a elegir\n"))
# print(menuE)
# y=int(input("Por favor introduzca la escuderia a elegir\n"))
# print(menuC)
# z=int(input("Por favor introduzca el conductor a elegir\n"))
x=1
y=1
z=1

a = Jugadores(x,cars[y],Cnd[z])

newCnd=Cnd.copy()
newcars=cars.copy()
newCnd = [w for w in newCnd if Cnd[z] != w]
newcars = [w for w in newcars if cars[y] != w]

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

# a.rival(rivals)
# a.copiar()
a.mostrar(players)

time.sleep(5)    
print(" ")

os.system('pause')




