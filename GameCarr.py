import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')



class jugadores:
	conductor=0
	carro=0 
	carril=0

	def _init_ (self,a,b,c):
		self.conductor=a
		self.carro=b
		self.carril=c

	def mostrar(x):
		print("nuestro jugador ",x," juega con el conductor ",self.conductor,"que lleva el carro ",self.carro,"y le fue asignado el carril ",self.carril)



lst=[] # lista de jugadores
pista=random.randint(10, 100) 
d='y' # variable para la Desicion de aceptar mas jugadores comienza como YES
print("Bienvenido al juego de los carros\n")
print("La pista a recorrer tiene\n", pista*100,"mts")
time.sleep(1)
players=random.randint(2, 6) 
print("El numero de autos compitiendo son\n", players,"autos")
# while d!='n':
# 	N=input("Escriba el nombre de jugador \n")
# 	lst.append(N)
# 	d=input("Desea agregar otro jugador Y o N \n").lower() 
# 	pass



print(random.randint(0, 6)) #dado
print(lst)
time.sleep(1)
os.system('cls')
