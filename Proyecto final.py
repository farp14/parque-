import pygame
from pygame.locals import *
import random

#INICIO pygame
pygame.init()
Screen = pygame.display.set_mode ((640,640))
#colores del juego
Color_fondo = 172, 180, 213
Color_ficha_azul = 63, 96, 226
Color_ficha_verde = 73, 226, 63
Color_ficha_amarilla =  202, 193, 85
Color_ficha_roja = 240, 48, 6
Color_escalones = 149, 155, 182
Color_cuadro_azul= 41, 61, 153
Color_cuadro_rojo = 153, 56, 41
Color_cuadro_amarillo = 230, 236, 104
Color_cuadro_verde = 176, 236, 104
Color_casilla = 229, 231, 233
#Diccionarios caminos de las fichas 

recorrido_azul = { "inicio": (225,100),
    "ruta": [(225,100),
        (225,130), (225,160), (225,190), (225,220),  # Sube en la columna 225
        (220,254),  # Gira a la izquierda  
        (190,225), (160,225), (130,225), (100,225), (70,225), (40,225), (10,225),  # Se mueve a la izquierda
        (10,290),   # seguro amarillo  
        (10,355), (40,355), (70,355), (100,355), (130,355), (160,355), (190,355), (220,355),  # Gira a la derecha y sube
        (249,390),  # Gira a la derecha y baja  
        (225,420), (225,450), (225,480), (225,510), (225,540), (225,570), (225,600),  # Baja hasta 225,600  
        (290,600),  #Seguro verde
        (355,600), (355,570), (355,540), (355,510), (355,480), (355,450), (355,420), (355,390),  # Sube hasta 355,390  
        (390,355),  # Gira a la derecha  
        (420,355), (450,355), (480,355), (510,355), (540,355), (570,355), (600,355),  # Baja hasta 390,600  
        (600,290),(600,225),  # Gira a la izquierda  
        (570,225), (540,225), (510,225), (480,225), (450,225), (420,225), (390,225), 
        (390,252),  # Sube en la columna 390  
        (355,220), (355,190), (355,160), (355,130), (355,100), (355, 70),(355,40),(355,10),  # Baja hasta 355,20  
        (290,10),  # Gira a la derecha hasta casilla azul  
        (290,40), (290,70), (290,100), (290,130), (290,160), (290,190), (290,220)  # Gira a la derecha hasta la última azul
    ],
    "meta": (290,220),
    "seguros": [
        (225,100), (100,225), (100,355), (225,510), (355,510), (510,355), (510,225), (355,100)
    ],
    "final": (320,320)  # Centro del cuadro de 138x138 
    }
recorrido_amarillo ={"inicio": (100,355),
        "ruta":[(100,355),
        (130,355), (160,355), (190,355), (220,355), 
        (249,390),  # Gira a la derecha y baja  
        (225,420), (225,450), (225,480), (225,510), (225,540), (225,570), (225,600),  # Baja hasta 225,600  
        (290,600),  #Seguro verde
        (355,600), (355,570), (355,540), (355,510), (355,480), (355,450), (355,420), (355,390),  # Sube hasta 355,390  
        (390,355),  # Gira a la derecha  
        (420,355), (450,355), (480,355), (510,355), (540,355), (570,355), (600,355),  # Baja hasta 390,600  
        (600,290),#seguro rojo
        (600,225), (570,225), (540,225), (510,225), (480,225), (450,225), (420,225), (390,225), 
        (390,252),  # Sube en la columna 390  
        (355,220), (355,190), (355,160), (355,130), (355,100), (355, 70),(355,40),(355,10),  # Baja hasta 355,20  
        (290,10),  # Gira a la derecha hasta casilla azul  
        (225,10),(225,40),(225,70),(225,100),(225,130), (225,160), (225,190), (225,220), # Sube en la columna 225
        (220,254),  # Gira a la izquierda  
        (190,225), (160,225), (130,225), (100,225), (70,225), (40,225), (10,225),  # Se mueve a la izquierda
        (10,290),   # seguro amarillo
        (40,290),(70,290),(100,290),(130,290),(160,290),(190,290),(220,290)],
        "seguros": [
        (225,100), (100,225), (100,355), (225,510), (355,510), (510,355), (510,225), (355,100)],
        "final": (320,320) }
recorrido_verde ={"inicio": (355,510),
                  "ruta":[(355,510), (355,480), (355,450), (355,420), (355,390),  # Sube hasta 355,390  
        (390,355),  # Gira a la derecha  
        (420,355), (450,355), (480,355), (510,355), (540,355), (570,355), (600,355),  # Baja hasta 390,600  
        (600,290),(600,225),  # Gira a la izquierda  
        (570,225), (540,225), (510,225), (480,225), (450,225), (420,225), (390,225), 
        (390,252),  # Sube en la columna 390  
        (355,220), (355,190), (355,160), (355,130), (355,100), (355, 70),(355,40),(355,10),  # Baja hasta 355,20  
        (290,10),  # Gira a la derecha hasta casilla azul  
        (225,10),(225,40),(225,70),(225,100),(225,130), (225,160), (225,190), (225,220), # Sube en la columna 225
        (220,254),  # Gira a la izquierda  
        (190,225), (160,225), (130,225), (100,225), (70,225), (40,225), (10,225),  # Se mueve a la izquierda
        (10,290), #seguro amarillo
        (10,355), (40,355), (70,355), (100,355), (130,355), (160,355), (190,355), (220,355),  # Gira a la derecha y sube
        (249,390),  # Gira a la derecha y baja  
        (225,420), (225,450), (225,480), (225,510), (225,540), (225,570), (225,600),  # Baja hasta 225,600  
        (290,600), #Seguro verde
        (290,570),(290,540),(290,510),(290,480),(290,450),(290,420),(290,390)],
        "seguros": [(225,100), (100,225), (100,355), (225,510), (355,510), (510,355), (510,225), (355,100)],
        "final":(320,320)}
recorrido_rojo = {"inicio": (510,225),
                                  "ruta":[(510,225), (480,225), (450,225), (420,225), (390,225), 
        (390,252),  # Sube en la columna 390  
        (355,220), (355,190), (355,160), (355,130), (355,100), (355, 70),(355,40),(355,10),  # Baja hasta 355,20  
        (290,10),  # Gira a la derecha hasta casilla azul  
        (225,10),(225,40),(225,70),(225,100),(225,130), (225,160), (225,190), (225,220), # Sube en la columna 225
        (220,254),  # Gira a la izquierda  
        (190,225), (160,225), (130,225), (100,225), (70,225), (40,225), (10,225),  # Se mueve a la izquierda
        (10,290), #seguro amarillo
        (10,355), (40,355), (70,355), (100,355), (130,355), (160,355), (190,355), (220,355),  # Gira a la derecha y sube
        (249,390),  # Gira a la derecha y baja  
        (225,420), (225,450), (225,480), (225,510), (225,540), (225,570), (225,600),  # Baja hasta 225,600  
        (290,600),  #Seguro verde
        (355,600), (355,570), (355,540), (355,510), (355,480), (355,450), (355,420), (355,390),  # Sube hasta 355,390  
        (390,355),  # Gira a la derecha  
        (420,355), (450,355), (480,355), (510,355), (540,355), (570,355), (600,355),  # Baja hasta 390,600  
        (600,290), #seguro rojo
        (570,290),(540,290),(510,290),(480,290),(450,290),(420,290),(390,290) ],
        "seguros": [
        (225,100), (100,225), (100,355), (225,510), (355,510), (510,355), (510,225), (355,100)],
        "final":(320,320)}

#posicion inicio de fichas 

fichas_azul = [(80,80), (150,80), (80,150), (150,150)]
fichas_amarillo = [(80,450), (150,450), (80,520), (150, 520)]
fichas_verde = [(450,450), (520,450), (450,520 ),(530,530) ]
fichas_rojo = [(450,80), (520, 80), (450,150), (520,150)]
fichas_cuadros = [fichas_azul,fichas_amarillo,fichas_rojo,fichas_verde]
#Tablero
"""Esta función visualiza cada casilla del tablero mediante la biblioteca Pygame, que permite dibujar rectángulos utilizados como casillas."""
def tablero ():
    Screen.fill (Color_fondo)
    pygame.draw.rect(Screen, Color_cuadro_azul,(10, 10, 210,210) )
    pygame.draw.rect(Screen, Color_cuadro_rojo,(420, 10, 210,210) )
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(10, 420, 210,210) )
    pygame.draw.rect(Screen, Color_cuadro_verde,(420, 420, 210,210) )

    pygame.draw.rect(Screen, Color_casilla,(355,10,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,40,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,70,60,29))

    pygame.draw.rect(Screen, Color_casilla,(355,130,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,160,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,190,60,29))


    pygame.draw.rect(Screen, Color_cuadro_azul,(290, 10, 60, 29))
    pygame.draw.rect(Screen, Color_cuadro_azul,(290, 40, 60, 29))
    pygame.draw.rect(Screen, Color_cuadro_azul,(290, 70, 60, 29))
    pygame.draw.rect(Screen, Color_cuadro_azul,(290, 100, 60, 29))
    pygame.draw.rect(Screen, Color_cuadro_azul,(290, 130, 60, 29))
    pygame.draw.rect(Screen, Color_cuadro_azul,(290, 160, 60, 29))
    pygame.draw.rect(Screen, Color_cuadro_azul,(290, 190, 60, 29))
    pygame.draw.rect(Screen, Color_cuadro_azul,(290, 220, 60, 29))
    pygame.draw.rect(Screen,Color_casilla,(225,10,60,29 )   )
    pygame.draw.rect(Screen,Color_casilla,(225,40,60,29 )   )
    pygame.draw.rect(Screen,Color_casilla,(225,70,60,29 )   )
    #Inicio recorrido ficha azul
    pygame.draw.rect(Screen,Color_casilla,(225,130,60,29 )   )
    pygame.draw.rect(Screen,Color_casilla,(225,160,60,29 )   )
    pygame.draw.rect(Screen,Color_casilla,(225,190,60,29 )   )

    pygame.draw.rect(Screen,Color_casilla,(249,220,36,29 )   )
    pygame.draw.polygon(Screen, Color_casilla,[(225, 220), (248, 220), (252,249)  ] )

    pygame.draw.rect(Screen,Color_casilla,(220,252,29,33 )   )
    pygame.draw.polygon(Screen, Color_casilla,[(220, 225), (220, 252), (249,252)  ] )

    pygame.draw.rect(Screen, Color_casilla,(10,225,29,60))
    pygame.draw.rect(Screen, Color_casilla,(40,225,29,60))
    pygame.draw.rect(Screen, Color_casilla,(70,225,29,60))

    pygame.draw.rect(Screen, Color_casilla,(130,225,29,60))
    pygame.draw.rect(Screen, Color_casilla,(160,225,29,60))
    pygame.draw.rect(Screen, Color_casilla,(190,225,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(10,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(40,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(70,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(100,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(130,290,29,60)) 
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(160,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(190,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(220,290,29,60))
    pygame.draw.rect(Screen, Color_casilla,(10,355,29,60))
    pygame.draw.rect(Screen, Color_casilla,(40,355,29,60))
    pygame.draw.rect(Screen, Color_casilla,(70,355,29,60)) 

    pygame.draw.rect(Screen, Color_casilla,(130,355,29,60))
    pygame.draw.rect(Screen, Color_casilla,(160,355,29,60))
    pygame.draw.rect(Screen, Color_casilla,(190,355,29,60))



    pygame.draw.rect(Screen, Color_casilla,(220,355,29,33))
    pygame.draw.polygon(Screen, Color_casilla,[(220,415), (220,387), (249, 387)  ] )


    pygame.draw.rect(Screen,Color_casilla,(249,390,36,29 )   )
    pygame.draw.polygon(Screen, Color_casilla,[(225, 418), (248, 418), (248,390)  ] )





    pygame.draw.rect(Screen, Color_casilla,(225,600,60,29))
    pygame.draw.rect(Screen, Color_casilla,(225,570,60,29))
    pygame.draw.rect(Screen, Color_casilla,(225,540,60,29))

    pygame.draw.rect(Screen, Color_casilla,(225,480,60,29)) 
    pygame.draw.rect(Screen, Color_casilla,(225,450,60,29))
    pygame.draw.rect(Screen, Color_casilla,(225,420,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(290,600,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(290,570,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(290,540,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(290,510,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(290,480,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(290,450,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(290,420,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(290,390,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,600,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,570,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,540,60,29))

    pygame.draw.rect(Screen, Color_casilla,(355,480,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,450,60,29))
    pygame.draw.rect(Screen, Color_casilla,(355,420,60,29))

    pygame.draw.rect(Screen,Color_casilla,(355,390,36,29 )   )
    pygame.draw.polygon(Screen, Color_casilla,[(391, 418), (391, 390), (415,418)  ] )

    pygame.draw.rect(Screen, Color_casilla,(390,355,29,36))
    pygame.draw.polygon(Screen, Color_casilla,[(390,385), (418 ,385), (418, 410)  ] )
    pygame.draw.rect(Screen, Color_casilla,(600,355,29,60))
    pygame.draw.rect(Screen, Color_casilla,(570,355,29,60))
    pygame.draw.rect(Screen, Color_casilla,(540,355,29,60))

    pygame.draw.rect(Screen, Color_casilla,(480,355,29,60))
    pygame.draw.rect(Screen, Color_casilla,(450,355,29,60))
    pygame.draw.rect(Screen, Color_casilla,(420,355,29,60))

    pygame.draw.rect(Screen, Color_cuadro_rojo,(600,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(570,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(540,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(510,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(480,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(450,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(420,290,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(390,290,29,60))
    pygame.draw.rect(Screen, Color_casilla,(600,225,29,60))
    pygame.draw.rect(Screen, Color_casilla,(570,225,29,60))
    pygame.draw.rect(Screen, Color_casilla,(540,225,29,60))

    pygame.draw.rect(Screen, Color_casilla,(480,225,29,60))
    pygame.draw.rect(Screen, Color_casilla,(450,225,29,60))
    pygame.draw.rect(Screen, Color_casilla,(420,225,29,60))


    pygame.draw.rect(Screen,Color_casilla,(390 ,252,29,33 )   )
    pygame.draw.polygon(Screen, Color_casilla,[(418, 227), (390, 252), (418,252)  ] )


    pygame.draw.rect(Screen,Color_casilla,(355,220,36,29 )   )
    pygame.draw.polygon(Screen, Color_casilla,[(391, 220), (391, 248), (415,220)  ] )

    pygame.draw.rect(Screen, Color_casilla,(251, 251, 138,138 ))

    #Salidas jugadores
    pygame.draw.rect(Screen,Color_cuadro_azul,(225,100,60,29 )   )
    pygame.draw.rect(Screen, Color_cuadro_azul,(100,225,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(100,355,29,60))
    pygame.draw.rect(Screen, Color_cuadro_amarillo,(225,510,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(355,510,60,29))
    pygame.draw.rect(Screen, Color_cuadro_verde,(510,355,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(510,225,29,60))
    pygame.draw.rect(Screen, Color_cuadro_rojo,(355,100,60,29))
tablero ()      
modo_juego=int(input ("quiere jugar como jugador marque 1, si es creador marque 2 "))

# Función para lanzar los dados
"""Esta función, aunque incompleta debido a un error no resuelto que afectó la regla de repetición de turno, tiene dos características importantes:
Permite elegir entre el modo creador y el modo jugador.
En el modo creador, se pueden ingresar los números de los dados.
En el modo jugador, los números se generan aleatoriamente mediante la función random.randint() de la biblioteca random, estableciendo límites entre 1 y 6."""

def lanzar_dados (repeticionnumero, modo_juego):
    if modo_juego ==1:
        print ("Ha elegido el modo jugador")
        dado_1 =(random.randint (1,6))
        dado_2 = (random.randint(1,6))
        dados = [dado_1 ,dado_2]
        if dado_2 == dado_1:
           if numero_dado1 == numero_dado2:
                repeticionnumero=+1
                if repeticionnumero ==3:
                
              
                    
                    print(f'se ha enviado a la casa la ficha de {jugador["nombre"] }')
                    ultima_ficha = pares_consecutivos["Ultima_ficha_movida"]["ultima_ficha"]
                    jugador["fichas"][ultima_ficha] = "casa"
                    print(f'se ha enviado a la casa la ficha de {jugador["nombre"] }')
                    pares_consecutivos["numero_de_pares"] = 0
                    dados = (numero_dado1, numero_dado2)    
                    return dados, repeticionnumero
                return dados, repeticionnumero
        return dados, repeticionnumero      
                        
               
               
        
    elif modo_juego == 2:
        print("Ha elegido el modo creador")
        numero_dado1 = int(input("ingrese un numero en 1 y 6 del primer dado"))
        numero_dado2 = int(input("Ingrese un numero entre 1 y 6 del segundo dado"))
        dados = (numero_dado1, numero_dado2)
        if 1 > numero_dado1 > 6 or 1 > numero_dado2 > 6:
            print ("Numeros invalidos, se va a continuar en modo jugador")
            return (random.randint (1,6),random.randint(1,6))
        else:
            
            if numero_dado1 == numero_dado2:
                repeticionnumero=+1
                if repeticionnumero ==3:
                
              
                    
                    print(f'se ha enviado a la casa la ficha de {jugador["nombre"] }')
                    ultima_ficha = pares_consecutivos["Ultima_ficha_movida"]["ultima_ficha"]
                    jugador["fichas"][ultima_ficha] = "casa"
                    print(f'se ha enviado a la casa la ficha de {jugador["nombre"] }')
                    pares_consecutivos["numero_de_pares"] = 0
                    dados = (numero_dado1, numero_dado2)    
                    return dados, repeticionnumero
                return dados, repeticionnumero
                
                        
        return dados, repeticionnumero
    

                
repeticionnumero=[]     
                    

    


# Función para crear un jugador
"""Esta función crea un diccionario para cada jugador, almacenando información como nombre, color, recorrido y fichas.
 Los datos se obtienen de las entradas del jugador y de otros diccionarios mediante un ciclo"""
def crear_jugador(nombre, color, recorrido, ficha_cuadros,):
    return {
        "nombre": nombre,
        "color": color,
        "recorrido": recorrido,
        "fichas_cuadros": ficha_cuadros,
        "fichas": ["casa","casa", "casa", "casa"]
    }
#FUNCION MOVER FICHAS
"""Esta función es fundamental para el juego, ya que recrea el movimiento de las fichas. Recibe como parámetros el diccionario del jugador, la ficha a mover y el resultado de los dados.
Utiliza condicionales para aplicar las reglas del juego, gestionar el avance de las fichas y realizar bloqueos."""
def mover_ficha(jugador, fichapos, pasos,):
    

    if jugador["fichas"][fichapos] == "casa":
        print (f'pasos{pasos}')   
             
        if 5 not in pasos and sum (pasos) != 5:
            print ("No sale ningua ficha, no has sacado 5")
            return
        elif 5 in pasos:
            
          jugador["fichas"][fichapos] =sum (pasos) -5
          nueva_posicion = jugador["fichas"][fichapos] =sum (pasos) -5
    
        else:
            print (sum(pasos)) 
            if sum (pasos) == 5:
                jugador["fichas"][fichapos] = 0
                nueva_posicion = jugador["fichas"][fichapos]
        for otra_ficha, otra_ficha_posicion in enumerate(jugador["fichas"]):
            if otra_ficha_posicion == nueva_posicion and otra_ficha != fichapos :
                 bloqueo = True
                 print ("Hizo un bloqueo")
                 break 

        
    else:
        nueva_posicion = jugador["fichas"][fichapos] + sum(pasos)
        if nueva_posicion < len(jugador["recorrido"]["ruta"]): 
            paso_faltantes = (len(jugador["recorrido"]["ruta"]) - nueva_posicion) 
            bloqueo = False
            for otra_ficha, otra_ficha_posicion in enumerate(jugador["fichas"]):
                if otra_ficha_posicion == nueva_posicion and otra_ficha != fichapos:
                    bloqueo = True

                    print ("Hizo un bloqueo")
                    return 
                    break
            
            if bloqueo:
                print("hay un bloqueo en esa posicion, pierde su turno")
                return 
            for otro_jugador in jugadores:
                if otro_jugador != jugador:
                    for otra_ficha in range (4):
                        if otro_jugador["fichas"][otra_ficha] == nueva_posicion:
                            otro_jugador ["fichas"][otra_ficha] = "casa"
                            print (f'la ficha de de {otro_jugador["nombre"]} ha sido enviada a casa ')
                            nueva_posicion +=10
                            if nueva_posicion == ((len(jugador["recorrido"]["ruta"]))+1):
                                jugador ["fichas"][fichapos] = "meta"
                                print ("La ficha ha sido coronada")
                                print (f"La ficha {(fichapos)+1}  ha sido coronada. Elija una ficha diferente para avanzar  10 casillas")
                                ficha_elegida = int(input ("Cual es la ficha que quiere avanzar las 10 casillas"))
                                mover_ficha (jugadores [turno_jugador], ficha_elegida, [10])
                    
                                return 
                            else:
                                
                                ficha_elegida = int(input ("Cual es la ficha que quiere avanzar las 10 casillas"))
                                mover_ficha (jugadores [turno_jugador], ficha_elegida, [10])
                    
                            
            jugador["fichas"][fichapos] = nueva_posicion
            if paso_faltantes < 8:
                print (f'a la fincha {jugador["fichas"]} le falta {paso_faltantes+1} ')
                paso_elegido =int (input (f"Uno de los dos valores de los dados para seguir avanzando {pasos}"))
                jugador["fichas"][fichapos]+=paso_elegido
                if jugador["fichas"][fichapos] == ((len(jugador["recorrido"]["ruta"])+1)):
                    jugador["fichas"][fichapos] = "meta"
                    print (f"La ficha {(fichapos)+1}  ha sido coronada. Elija una ficha diferente para avanzar  10 casillas")
                    ficha_elegida = int(input ("Cual es la ficha que quiere avanzar las 10 casillas"))
                    mover_ficha (jugadores [turno_jugador], ficha_elegida, [10])
                    
                else:
                    print ("No es posible ese movimiento, pierde su turno")
                    return 



# Función para dibujar una ficha
"""Esta función recibe como parámetros el jugador, la ficha y las posiciones de las fichas.
Estos parámetros ayudan a establecer la posición exacta de las fichas en el tablero y actualizan la información a medida que el juego avanza, mediante condicionales."""
def dibujar_ficha(jugador, ficha, posiciones_fichas):
    ficha_posicion = jugador["fichas"][ficha]
    if ficha_posicion == "casa":
        x, y = jugador["fichas_cuadros"][ficha] 
    elif ficha_posicion == "meta":
        x, y = jugador["recorrido"]["final"]
    else:
        x, y = jugador["recorrido"]["ruta"][ficha_posicion]
    

    if ficha_posicion in posiciones_fichas and len(posiciones_fichas[ficha_posicion]) > 1:
        
        pygame.draw.circle(Screen, jugador["color"], (x + 7, y + 7), 12)
    else:
        pygame.draw.circle(Screen, jugador["color"], (x+14, y+14), 12)

# Preguntar cuántos jugadores
num_jugadores = int(input("¿Cuántos jugadores? (2 o 4): "))
jugadores = []

# Crear jugadores según la cantidad ingresada
colores = [Color_ficha_azul, Color_ficha_amarilla, Color_ficha_verde, Color_ficha_roja]
recorridos = [recorrido_azul, recorrido_amarillo, recorrido_verde, recorrido_rojo]

for i in range(num_jugadores):
    nombre = input(f"Nombre del jugador {i + 1}: ")
    jugadores.append(crear_jugador(nombre, colores[i], recorridos[i], fichas_cuadros[i]))
print("Presiona la barra espaciadora en la pantalla del juego para iniciar")
# Variables del juego
turno_jugador = 0
dados_lanzados = False


# Bucle principal del juego
"""Este bucle, requerido por Pygame, mantiene la pantalla abierta y la actualiza constantemente durante el juego. 
También se encarga de cerrar el juego cuando es necesario."""
pygame.display.set_caption("Parques")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dados_lanzados:
                    print (f'TURNO DE{jugadores[turno_jugador]["nombre"]}')
                    print("Presiona la barra espaciadora para lanzar los dados.")   
                    dados, Pares_consecutivos = lanzar_dados(repeticionnumero, modo_juego)                 
                    print(f"Dados: {dados}")
                    dados_lanzados = True
                    print ("vuelve a presionar la barra espaciadora")
                    
                else:
                    print(f'TURNO DE {jugadores[turno_jugador]["nombre"]}')
                    ficha_a_mover = (int(input("¿Qué ficha mover? (1-4): ")) - 1)
                    Pares_consecutivos = mover_ficha(jugadores[turno_jugador], ficha_a_mover, dados,)
                    dados_lanzados = False
                    if dados[0] != dados[1]:
                        turno_jugador = (turno_jugador + 1) % num_jugadores
                        print("Presiona la barra espaciadora para pasar al siguiente jugador.")
                    else:
                        print("Sacaste pares, vuelve a lanzar.")
                        print("puls barra espaciadora")
                   
    posiciones_fichas = {}
    for jugador in jugadores:
        for ficha in jugador["fichas"]:
            if ficha != "casa" and ficha != "meta":
                if ficha not in posiciones_fichas:
                    posiciones_fichas[ficha] = []
                posiciones_fichas[ficha].append(jugador)

    tablero ()
    for jugador in jugadores:
        for i in range(4):
            dibujar_ficha(jugador, i,posiciones_fichas)
    
    pygame.display.update()

    



