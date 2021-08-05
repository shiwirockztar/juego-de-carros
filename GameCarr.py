import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')


lst=[] # lista de jugadores

d='y' # variable para la Desicion de aceptar mas jugadores comienza como YES
print("Bienvenido al juego de los carros\n")
while d!='n':
	N=input("Escriba el nombre de jugador \n")
	lst.append(N)
	d=input("Desea agregar otro jugador Y o N \n").lower() 
	pass
print(random.randint(0, 6)) #dado
print(lst)
time.sleep(1)
os.system('cls')
