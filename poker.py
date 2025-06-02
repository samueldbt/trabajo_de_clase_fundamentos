import random
import os
import itertools
# Palos y rangos
palos = ['♠', '♥', '♦', '♣']
rangos = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def crear_baraja():
    baraja = []
    for palo in palos:
        for rango in rangos:
            baraja.append([rango, palo]) #crea la baraja con su rango (como letrica o numerito) y palo (la familia pues)
    random.shuffle(baraja) #la mezcla
    return baraja # devuelve la baraja con 52 cartas (en formato de listas) con su palo y rango, el for de arriba se encarga de que sean 52 cartas exactas

def repartir(baraja, num_cartas): #reparte una mano (se hara para cada jugador claro)
    mano = []
    for _ in range(num_cartas):
        mano.append(baraja.pop()) #le da al jugador la carta que se quita de la baraja mezclada
    return mano #cuando tiene las 2 cartas por jugador se las devuelve al jugador respectivo

def mostrar_mano(mano):
    return " ".join([carta[0] + carta[1] for carta in mano]) #se concatenan las listas dentro de mano para mostrarlas bonitas con el join

def valor_rango(rango): #esto se usa en la funcion de evaluar mano no en la principal (juego)
    return valores[rangos.index(rango)] #le asigna un valor acada numerito o letra 

def contar_repetidos(mano): #esto se usa en la funcion de evaluar_mano no en la principal (juego)
    contador = []
    for carta in mano:
        existe = False #asume que la carta no se ha contado
        for i in range(len(contador)):
            if contador[i][0] == carta[0]:
                contador[i][1] += 1 #se dice que tiene la carta y se suma al numero de veces que ya habia salido la carta
                existe = True
        if not existe:
            contador.append([carta[0], 1])
    return contador #esto es util para saber si se tiene trios o pares o full houses y asi

def es_color(mano): #esto se usa en la funcion de evaluar_mano no en la principal (juego)
    primer_palo = mano[0][1] #toma el palo de la primera carta
    for carta in mano:
        if carta[1] != primer_palo:
            return False #si alguna carta es de un palo distinto devuelve false
    return True #sino quiere decir que tenemos un color

def es_escalera(valores_ordenados): #esto se usa en la funcion de evaluar_mano no en la principal (juego)
    for i in range(len(valores_ordenados) - 1):
        if valores_ordenados[i] - 1 != valores_ordenados[i + 1]: #mira la escalera
            return False
    return True

def evaluar_mano(mano): #esta funcion se usa dentro de la funcion de comparar mano, no en la funcion principal (la de juego)
    valores_mano = [valor_rango(carta[0]) for carta in mano] #le da un valor a cada carta
    valores_mano.sort(reverse=True) #ordena los valores de las cartas de mayor a menor (para eso e usar el reverse=True)
    repes = contar_repetidos(mano) #para ver pares y eso
    repes.sort(key=lambda x: (x[1], valor_rango(x[0])), reverse=True) #organiza las cartas repetidas en orden descendente, tipo las que mas se repiten primero y asi, para eso es el key=lambda

    if len(repes) == 1 and repes[0][1] == 5:
        return [9, valor_rango(repes[0][0])]  # Repóker

    if repes[0][1] == 4:
        return [7, valor_rango(repes[0][0])]  # Póker

    if len(repes) == 2 and repes[0][1] == 3 and repes[1][1] == 2:
        return [6, valor_rango(repes[0][0]), valor_rango(repes[1][0])]  # Full

    if es_color(mano):
        return [5, valores_mano]  # Color

    if es_escalera(valores_mano):
        return [4, valores_mano[0]]  # Escalera

    if repes[0][1] == 3:
        return [3, valor_rango(repes[0][0])]  # Trío

    if len(repes) >= 2 and repes[0][1] == 2 and repes[1][1] == 2:
        return [2, valor_rango(repes[0][0]), valor_rango(repes[1][0])]  # Doble pareja

    if repes[0][1] == 2:
        return [1, valor_rango(repes[0][0])]  # Pareja

    return [0, valores_mano]  # Carta alta

def comparar_manos(mano1, mano2): #devuelve cual mano es mas fuerte
    eval1 = evaluar_mano(mano1) #mira el valor de la mano primero
    eval2 = evaluar_mano(mano2) #mira el valor de la otra mano, la del otro jugador
    if eval1 > eval2: #y pues mira cual mano es mayor o mas fuerte
        return 1
    elif eval2 > eval1:
        return -1
    else:
        return 0

def mejor_mano_5cartas(cartas):
    mejores = None
    for combinacion in itertools.combinations(cartas, 5):
        evaluacion = evaluar_mano(list(combinacion))
        if (mejores is None) or (evaluacion > mejores):
            mejores = evaluacion
    return mejores

def pre_ronda(nombres, fichas, activos):
    print("\n--- Ronda pre-flop ---")
    apuestas = [0 for _ in nombres] #la apuesta inicial de cada jugador es 0
    pozo = 0
    ciega_minima = 0

    try: #esto es para ejecutar algo que podria fallar, si digamos el usuario aqui pone letras, el codigo va a ir al except de abajo
            cantidad = int(input(f"\n{nombres[0]} pon la ciega menor: "))
    except: #aqui dice lo que sea hace en el caso de que la instruccion de arriba falle, es super util por si pueden ocurrir cosas inesperadas que hagan fallar al codigo
        if cantidad == 0:
            cantidad = 1
    ciega_minima = cantidad

    #esto es para el resto de jugadores despues de la ciega
    for i in range(len(nombres[1:])): #slicing para evitar a la ciega minima
        #iguala, sube o retira
        accion = input("¿(i)igualar, (s)subir o (r)etirarte?: ").lower()
        if accion == "i":
            cantidad +=cantidad
            fichas[i] -= cantidad #se resta lo que se aposto de lo que se tenia
            apuestas[i] += cantidad #se le suma a lo apostado pues lo apostado xd
            pozo += cantidad #se le suma al pozo lo que se aposto
        elif accion == "s":
            cantidad = int(input("cuanto desea subir (minimo el doble de la ciega): "))
            if cantidad > fichas[i]: #aqui se trabaja con lo que se quiere apostar y lo que se tiene
                cantidad = fichas[i] #si apuesta mas de lo que tiene pues apuesta todo
            elif cantidad < cantidad + cantidad:
                print("cantidad insuficiente, aumentando la minima posible: ")
                cantidad = ciega_minima #debo mantener la ciega minima
                cantidad += cantidad
            fichas[i] -= cantidad #se resta lo que se aposto de lo que se tenia
            apuestas[i] += cantidad #se le suma a lo apostado pues lo apostado xd
            pozo += cantidad #se le suma al pozo lo que se aposto
        elif accion == "r":
            print("bye bye")
            activos[i] = False
            pozo = cantidad
            
        print(f"el pozo pre-flop es: {pozo}")

    return pozo, activos

def ronda_apuestas(nombres, fichas, activos, pozo):
    print("\n--- Ronda de Apuestas ---")
    apuestas = [0 for _ in nombres]
    apuesta_max = 0
    jugadores_pendientes = [i for i, activo in enumerate(activos) if activo]
    ya_actuaron = [False for _ in nombres]

    while True:
        cambios = False
        for i in jugadores_pendientes:
            if not activos[i]:
                continue
            print(f"\n{nombres[i]}, tienes {fichas[i]} fichas. Apuesta actual: {apuestas[i]}. Apuesta máxima: {apuesta_max}.")
            if apuesta_max == 0:
                accion = input("¿(a)postar, (p)asar o (r)etirarte?: ").lower()
            else:
                accion = input("¿(a)postar/igualar, (r)etirarte?: ").lower()
                if accion == 'p':
                    print("No puedes pasar si ya hay una apuesta. Debes igualar o retirarte.")
                    accion = input("¿(a)postar/igualar, (r)etirarte?: ").lower()
            if accion == 'r':
                activos[i] = False
                print(nombres[i], "se ha retirado.")
                cambios = True
            elif accion == 'a':
                if apuesta_max == 0:
                    try:
                        cantidad = int(input("¿Cuánto quieres apostar?: "))
                    except:
                        cantidad = 0
                    if cantidad > fichas[i]:
                        cantidad = fichas[i]
                    apuestas[i] += cantidad
                    fichas[i] -= cantidad
                    pozo += cantidad
                    apuesta_max = apuestas[i]
                    print(nombres[i], "apostó", cantidad)
                    cambios = True
                    ya_actuaron = [False for _ in nombres]
                    ya_actuaron[i] = True
                else:
                    diferencia = apuesta_max - apuestas[i]
                    extra = 0
                    try:
                        extra = int(input(f"¿Quieres subir la apuesta? Tu mínimo para igualar es {diferencia}. Si quieres subir, ingresa el total (mayor que {diferencia}), si solo igualas pon {diferencia}: "))
                    except:
                        extra = diferencia
                    if extra < diferencia:
                        extra = diferencia
                    if extra > fichas[i]:
                        extra = fichas[i]
                    apuestas[i] += extra
                    fichas[i] -= extra
                    pozo += extra
                    if apuestas[i] > apuesta_max:
                        apuesta_max = apuestas[i]
                        ya_actuaron = [False for _ in nombres]
                        ya_actuaron[i] = True
                        cambios = True
                    else:
                        ya_actuaron[i] = True
            elif accion == 'p' and apuesta_max == 0:
                print(nombres[i], "pasó.")
                ya_actuaron[i] = True
            else:
                print("Opción no válida. Se considera que pasaste si es posible, o igualas si hay apuesta.")
                if apuesta_max == 0:
                    ya_actuaron[i] = True
                else:
                    diferencia = apuesta_max - apuestas[i]
                    if diferencia > fichas[i]:
                        diferencia = fichas[i]
                    apuestas[i] += diferencia
                    fichas[i] -= diferencia
                    pozo += diferencia
                    ya_actuaron[i] = True
        jugadores_pendientes = [i for i, activo in enumerate(activos) if activo and apuestas[i] != apuesta_max]
        if len([a for i,a in enumerate(activos) if a]) <= 1:
            break
        if all(ya_actuaron[i] or not activos[i] for i in range(len(nombres))) and len(jugadores_pendientes) == 0:
            break
    return pozo, activos

def mostrar_comunitarias(comunitarias, cuantas):
    print("\nCartas comunitarias:")
    for i in range(cuantas):
        print(comunitarias[i][0] + comunitarias[i][1], end=" ")
    print()

def juego(): #funcion principal, esto contiene todas las funciones declaradas anteriormente y activa la partida como tal
    nombres = input("Nombres de jugadores separados por coma: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    fichas = [1000 for _ in nombres] #le da la plata a cada jugador
    dealer = 0 #para rotar el dealer o el que reparte

    while all(f > 0 for f in fichas): #mientras hayan fichas
        print("\n=== Nueva Mano ===")
        baraja = crear_baraja()
        manos = []
        activos = [True for _ in nombres] #genera una lista con un True por cada jugador que sigue en la partida

        #fase 0: preflop
        pozo, activos = pre_ronda(nombres, fichas, activos)

        for _ in nombres:
            manos.append(repartir(baraja, 2)) #se le dan las cartas a cada jugador
        comunitarias = repartir(baraja, 5)
        cartas_mostradas = 0
        pozo_total = 0 #esto es para llevar la cuenta de la apuesta en la mesa a lo largo de las rondas

        # Mostrar cartas personales una por una
        print("\n--- Cartas Iniciales ---")
        for i in range(len(nombres)): #primero un jugador luego el otro
            input(f"\nTurno de {nombres[i]}. Presiona Enter para ver tus cartas.")
            print(f"Tus cartas: {mostrar_mano(manos[i])}")
            input("Presiona Enter para ocultar tus cartas.")
            os.system("cls" if os.name == "nt" else "clear")  #esta funcion es para limpiar la terminal asi evitamos hacer un millon de saltos de linea feos, el "nt" refiere a windows y el else es por si es otro os
                                                              #el os detecta sistema operativo y ejecuta cls que es para limpiar la terminal en windows

        # Fase 1: Flop
        cartas_mostradas += 3
        mostrar_comunitarias(comunitarias, cartas_mostradas)
        pozo, activos = ronda_apuestas(nombres, fichas, activos, pozo)
        pozo_total += pozo #se le suma pues lo de la ronda 

        # Fase 2: Turn
        vivos = [i for i in range(len(nombres)) if activos[i]] #checa los jugadores que siguen en el juego despues del flop
        if len(vivos) > 1:
            cartas_mostradas += 1
            mostrar_comunitarias(comunitarias, cartas_mostradas) #muestra una cartita mas
            pozo, activos = ronda_apuestas(nombres, fichas, activos, pozo)
            pozo_total += pozo #igual que en la 163 xd

        # Fase 3: River
        vivos = [i for i in range(len(nombres)) if activos[i]] #no se que es river xd pero igual se checan los activos en la ronda actual
        if len(vivos) > 1:
            cartas_mostradas += 1
            mostrar_comunitarias(comunitarias, cartas_mostradas)
            pozo, activos = ronda_apuestas(nombres, fichas, activos, pozo)
            pozo_total += pozo #hasta aca igual que arriba

        # Mostrar ganador
        vivos = [i for i in range(len(nombres)) if activos[i]] #vuelve a mirar los activos ya que estan las 5 cartas sobre la mesa
        if len(vivos) == 1:
            ganador = vivos[0] #gana el que queda vivo en caso de que todos se hubieran retirado
            print(f"\n{nombres[ganador]} gana el pozo porque los demás se retiraron.")
        else:
            mejor = mejor_mano_5cartas(manos[vivos[0]] + comunitarias) 
            ganador = vivos[0] #esto es como un marcador para orita compara mano por mano
            print("\n--- Mostrar manos ---")
            for i in vivos: #compara todos los jugadores que siguen en la partida
                actual_eval = mejor_mano_5cartas(manos[i] + comunitarias) #marcador para ir uno a uno
                print(f"{nombres[i]} tiene: {mostrar_mano(manos[i])}")
                if actual_eval > mejor: #si la mano del jugador que se tiene en actual es mas fuerte que la del mejor (que por defecto es el primero de la lista)
                    mejor = actual_eval #el mejor pasa a ser el que se esta comparando actualmente
                    ganador = i #ganador se vuelve un marcador del jugador actual
            print(f"\n{nombres[ganador]} gana el pozo con la mejor mano.")

        fichas[ganador] += pozo_total #se le suma las ganancias a las fichas del ganador
        dealer = (dealer + 1) % len(nombres) #esto es para pasar el turno del que va primero y asi en el juego
        input("Presiona Enter para continuar...") #al presionar enter pues se repite otra vez, pasa a otra ronda
        os.system("cls" if os.name == "nt" else "clear") #limpia la terminal para la siguiente ronda uwus
juego()
