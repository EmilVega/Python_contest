import random as rnd

ANCHO = 25
ALTO = 25
MURO = 1
HUECO = 0
SALIDA = 2
META = 3

listaDireccion =[]

def CambiarDireccion(mapa,x,y,antiguaDireccion):
	#print(listaDireccion)
	if mapa[y][x+1]==HUECO or mapa[y][x+1]==META:
		if mapa[y][x+1]==META:
			direccion= "E"
		else:		
			direccion= "E"
			mapa[y][x+1]=0.5
			listaDireccion.append("W")
	elif mapa[y+1][x]==HUECO or mapa[y+1][x]==META:
		if mapa[y+1][x]==META:
			direccion= "S"
		else:
			direccion= "S"
			mapa[y+1][x]=0.5
			listaDireccion.append("N")
	elif mapa[y][x-1]==HUECO or mapa[y][x-1]==META:
		if mapa[y][x-1]==META:
			direccion="W"
		else:
			direccion="W"
			mapa[y][x-1]=0.5
			listaDireccion.append("E")		
	elif mapa[y-1][x]==HUECO or mapa[y-1][x]==META:
		if mapa[y-1][x]==META:
			direccion="N"
		else:
			direccion="N"
			mapa[y-1][x]=0.5
			listaDireccion.append("S")
	else:
		direccion = listaDireccion[len(listaDireccion)-1]
		listaDireccion.pop()	
	
	return (mapa, direccion)




			


#	direccion = rnd.randint(0,7)
#	if (direccion==0): return(mapa,antiguaDireccion)
#	elif (direccion==1): return(mapa,"N")
#	elif (direccion==2 or direccion==3): return(mapa,"S")
#	elif (direccion==4 or direccion==5): return(mapa,"E")
#	else: return(mapa,"W")
#def CambiarDireccion(mapa):
