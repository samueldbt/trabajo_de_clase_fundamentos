import random
import os
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

def ronda_apuestas(nombres, fichas, activos):
    print("\n--- Ronda de Apuestas ---")
    apuestas = [0 for _ in nombres] #la apuesta inicial es 0
    pozo = 0

    for i in range(len(nombres)):
        if not activos[i]: #si un jugador no esta activo sigue de largo
            continue
        print(f"\n{nombres[i]}, tienes {fichas[i]} fichas.")
        accion = input("¿(a)postar, (p)asar o (r)etirarte?: ").lower() #se decide la accion del jugador con condicionales y se usar .lower para evitar errores tipograficos
        if accion == 'r':
            activos[i] = False #cambia el estado del jugador
            print(nombres[i], "se ha retirado.")
        elif accion == 'a':
            try: #esto es para ejecutar algo que podria fallar, si digamos el usuario aqui pone letras, el codigo va a ir al except de abajo
                cantidad = int(input("¿Cuánto quieres apostar?: "))
            except: #aqui dice lo que sea hace en el caso de que la instruccion de arriba falle, es super util por si pueden ocurrir cosas inesperadas que hagan fallar al codigo
                cantidad = 0
            if cantidad > fichas[i]: #aqui se trabaja con lo que se quiere apostar y lo que se tiene
                cantidad = fichas[i] #si apuesta mas de lo que tiene pues apuesta todo
            fichas[i] -= cantidad #se resta lo que se aposto de lo que se tenia
            apuestas[i] += cantidad #se le suma a lo apostado pues lo apostado xd
            pozo += cantidad #no se que es el pozo mano xd pero se le suma lo que se aposto
            print(nombres[i], "apostó", cantidad)
        elif accion == 'p':
            print(nombres[i], "pasó.")
        else:
            print("Opción no válida. Se considera que pasaste.") #cuando no se digita ninguna de la opciones que son
    return pozo, activos #no sabia que se podian devolver 2 variables asi xd

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
            os.system("cls" if os.name == "nt" else clear)  #esta funcion es para limpiar la terminal asi evitamos hacer un millon de saltos de linea feos, el "nt" refiere a windows y el else es por si es otro os
                                                            #el os detecta sistema operativo y ejecuta cls que es para limpiar la terminal en windows

        # Fase 1: Flop
        cartas_mostradas += 3
        mostrar_comunitarias(comunitarias, cartas_mostradas)
        pozo, activos = ronda_apuestas(nombres, fichas, activos)
        pozo_total += pozo #se le suma pues lo de la ronda 

        # Fase 2: Turn
        vivos = [i for i in range(len(nombres)) if activos[i]] #checa los jugadores que siguen en el juego despues del flop
        if len(vivos) > 1:
            cartas_mostradas += 1
            mostrar_comunitarias(comunitarias, cartas_mostradas) #muestra una cartita mas
            pozo, activos = ronda_apuestas(nombres, fichas, activos)
            pozo_total += pozo #igual que en la 163 xd

        # Fase 3: River
        vivos = [i for i in range(len(nombres)) if activos[i]] #no se que es river xd pero igual se checan los activos en la ronda actual
        if len(vivos) > 1:
            cartas_mostradas += 1
            mostrar_comunitarias(comunitarias, cartas_mostradas)
            pozo, activos = ronda_apuestas(nombres, fichas, activos)
            pozo_total += pozo #hasta aca igual que arriba

        # Mostrar ganador
        vivos = [i for i in range(len(nombres)) if activos[i]] #vuelve a mirar los activos ya que estan las 5 cartas sobre la mesa
        if len(vivos) == 1:
            ganador = vivos[0] #gana el que queda vivo en caso de que todos se hubieran retirado
            print(f"\n{nombres[ganador]} gana el pozo porque los demás se retiraron.")
        else:
            mejor = manos[vivos[0]] + comunitarias 
            ganador = vivos[0] #esto es como un marcador para orita compara mano por mano
            print("\n--- Mostrar manos ---")
            for i in vivos: #compara todos los jugadores que siguen en la partida
                actual = manos[i] + comunitarias #marcador para ir uno a uno
                print(f"{nombres[i]} tiene: {mostrar_mano(manos[i])}")
                if comparar_manos(actual, mejor) > 0: #si la mano del jugador que se tiene en actual es mas fuerte que la del mejor (que por defecto es el primero de la lista)
                    mejor = actual #el mejor pasa a ser el que se esta comparando actualmente
                    ganador = i #ganador se vuelve un marcador del jugador actual
            print(f"\n{nombres[ganador]} gana el pozo con la mejor mano.")

        fichas[ganador] += pozo_total #se le suma las ganancias a las fichas del ganador
        dealer = (dealer + 1) % len(nombres) #esto es para pasar el turno del que va primero y asi en el juego
        input("Presiona Enter para continuar...") #al presionar enter pues se repite otra vez, pasa a otra ronda
        os.system("cls" if os.name == "nt" else clear) #limpia la terminal para la siguiente ronda uwus
juego()


