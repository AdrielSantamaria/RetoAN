#Adriel Jael Santamaria Hernandez
#A01753918

import math
import turtle
import random
import numpy as np


'''def buscar_codigo_limitado(intentos,a,b,coordenada):
    puntos=[]
    for i in range(intentos):
        coord = [round(a+(random.random()*random.choice((1,-1))*random.randint(1,4)),2),
                 round(b+(random.random()*random.choice((1,-1))*random.randint(1,4)),2)]
        angulo,distancia= calcular_distancia(coord,coordenada)
        turtle.pu()
        mover_rover(angulo,distancia)
        coordenada = coord
        puntos.append(coord)

    return puntos'''

  
  
def crear_pantalla():
    turtle.speed(0)
    turtle.setup(1000,980,900,1)
    turtle.bgcolor("black")
    turtle.title("Busqueda del ArUco")
    turtle.pencolor("white")
    turtle.goto(-500,0)
    turtle.fd(1000)
    turtle.pu()
    turtle.goto(0,-490)
    turtle.lt(90)
    turtle.pd()
    turtle.fd(1000)
    turtle.home()
    turtle.pencolor("white")
    turtle.dot(10,"orange")
    turtle.speed(6)
    turtle.pensize(2)
    

def generar_coordenada_aleatoria(a,b):
    x=(random.randint(a,b))
    y=(random.randint(a,b))    
    coordenada=[x,y]
    
    return coordenada
 
 
def calcular_distancia(c_final,c_inicial):
    xf=c_final[0]
    yf=c_final[1]
    x0=c_inicial[0]
    y0=c_inicial[1]
    distancia = abs(math.sqrt((xf-x0)**2+(yf-y0)**2))
    angulo = math.atan2(yf-y0,xf-x0)
    
    return math.degrees(angulo),distancia


def mover_rover(angulo,distancia):
    turtle.seth(angulo)
    imprimir_coordenadas(distancia)
    turtle.pd()
    turtle.dot(5)


def imprimir_coordenadas(distancia):
    anterior=0
    
    for i in np.arange(0.0,distancia+0.1, 0.11):
        turtle.fd((i-anterior)*15)
        coordenadas = [round(turtle.xcor()/15,2), round(turtle.ycor()/15,2)]
        print(coordenadas)
        
        anterior=i


def buscar_codigo_ciclo(x,y,coordenada,distancias):
    x_ar=round(x+(random.random()*random.choice((1,-1))*random.randint(1,4)),2)
    y_ar=round(y+(random.random()*random.choice((1,-1))*random.randint(1,4)),2)
    detectar = False
    
    while detectar == False:
            punto_aleatorio = [round(x+(random.random()*random.choice((1,-1))*random.randint(1,4)),2),
                               round(y+(random.random()*random.choice((1,-1))*random.randint(1,4)),2)]
            angulo,distancia = calcular_distancia(punto_aleatorio,coordenada)
            turtle.pu()
            print("Coordenadas al siguiente punto:")
            turtle.speed(0)
            mover_rover(angulo,distancia)
            coordenada = punto_aleatorio
            distancias = distancias+distancia
            detectar = detectar_codigo(coordenada,int(x_ar),int(y_ar))
            turtle.dot("red")
            
    print("El Rover encontro el ArUco en:",coordenada)
    turtle.dot(12,(0,1,0))
    
    return [x_ar,y_ar],distancias


def detectar_codigo(coordenada,x_ar,y_ar):
    detectar = False
    x = int(coordenada[0])
    y = int(coordenada[1])
    
    if x == x_ar and y == y_ar:
        detectar = True
        
    return detectar
    

def main():
    coordena_inicial= [0,0]
    coordenada = generar_coordenada_aleatoria(-25,25)
    angulo, distancia = calcular_distancia(coordenada,coordena_inicial)
    
    crear_pantalla()
    print("Coordenadas del origen al lugar aproximado del código:")
    mover_rover(angulo,distancia)
    print("Llegamos al lugar aproximado, procediendo busqueda...\n")
    punto_final,distancia_final = buscar_codigo_ciclo(coordenada[0],coordenada[1],coordenada,distancia)
    #puntos = buscar_codigo_limitado(5,int(coordenada[0]),int(coordenada[1]),coordenada)
    
    print("La posición exacta del ArUco es:",punto_final)
    print("El Rover recorrio",round(distancia_final,2),"metros, desde el punto:",coordena_inicial,"hasta:",punto_final)



main()
turtle.exitonclick()