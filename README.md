# RetoAN
Reto para Autonomous Navigation


La función "crear_pantalla" crea el screen de turtle con dimensiones delimitadas y un formato propuesto por su servidor. A su vez dibuja un plano cartesiano para que sea más fácil identificar la distancia de los puntos.

La función "generar_coordenada_aleatoria" recibe como variables de entrada un parametro en cual generara la coordenada (x,y) de un punto aproximado en el cual puede estar el codigo ArUco.

La función "calcular_distancia" hace operaciones matematicas para encontrar la distancia entre dos puntos y el angulo que necesita para empezar a moverse.

La función "mover_rover" recibe como variables de entrada el angulo y distancia que previamente se encontro y voltea a turtle con el angulo dado, llama a la funcion "imprimir_coordenadas" y dibuj un punto en el lugar al que llega 

La función "imprimir_coordenadas" utiliza un for para recorrer de 0 a la distancia que necesita recorrer con un paso de 0.11, hace avanzar a turtle (lo multiplica por 15 para poder visualizar el movimiento en la pantalla, de otra manera se veria muy pequeño, la proporción de los metros es 1:15) posteriormente guarda la posicion de turtle en coordenadas y la imprime cada que avanza el paso (de 0.11)

La función "buscar_codigo_ciclo" recibe como variable de entrada la coordenada "x" y "y" del punto aproximado, la coordenada completa y la distancia que ha recorrido hassta ese momento, de esta manera genera la coordenada exacta en (x,y) del codigo ArUco, lo genera a partir de la suma de la coordenada aproximada y un numero aleatorio de 1 a 4 para que este punto aparezca en un rango de 1 a 4 metros del punto aproximado. Posteriormente hace un ciclo el cual ggenera un punto aleatorio de la misma manera que se genero el punto exacto del códgio ArUco, se llama a la función "mover_rover", lo mueve hacia ese punto mientras se imprimen sus coordenadas, se suma esta distancia a las distancias acumuladas y se llama a la función "detectar_codigo" para saber si el punto generado es el mismo en el cual esta el codigo ArUco, si es asi, se detiene el ciclo y regresa a main()

La función "detectar_código" recibe como variables de entrada la coordenada donde se encuentra en ese momento el rover y la coordenada exacta del código ArUco. Verifica si las coordenadas en "x" y "y" de estos dos puntos son iguales, si es asi la variable detectar se vuelve verdadera y cuando regresa a la función que busca el codigo, detiene el ciclo.

La función "main" tiene la coordenada inicial, recibe la coordenada aproximada del código ArUco, recibe el angulo y distancia para mover el rover, llama a la función para crear la screen de turtle, imprimer descripciones y resultados. 


Finalmente hay una función que se llama "buscar_codigo_limitado" que busca el codigo ArUco, pero con ciertos intentos, lo inclui en el codigo como comentario como una opción secundaria del reto. 
