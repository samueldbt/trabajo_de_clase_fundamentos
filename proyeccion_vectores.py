#proyeccion d un vector w sobre dos vectores unitarios. Grafica de los 3.
import random
import math
import matplotlib.pyplot as plt

numero_vectores = int(input("cuantos vectores desea ingresar: "))

for i in range(numero_vectores):
    #generar el primer vector
    print(f"vector {i}: ")
    componente_x = float(input(f"componente x del vector {i}: "))
    componente_y = float(input(f"componente y del vector {i}: "))
    v = (componente_x, componente_y)
    
    #generar vectores unitarios
    angulo = random.uniform(0, 2 * math.pi)
    ux = math.cos(angulo)
    uy = math.sin(angulo)
    u = (ux, uy)

    angulo2 = random.uniform(0, 2 * math.pi)
    ux2 = math.cos(angulo2)
    uy2 = math.sin(angulo2)
    u2 = (ux2, uy2)
    
    #proyeccion sobre el primer vector unitario
    proyv_u = (((componente_x*ux) + (componente_y*uy)) * ux, ((componente_x*ux) + (componente_y*uy)) * uy)
    proyv_u2 = (((componente_x*ux2) + (componente_y*uy2)) * ux2, ((componente_x*ux2) + (componente_y*uy2)) * uy2)

    #configura la grafica de los vectores y la enseña en pantalla
    plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, color="yellow", label="v")
    plt.quiver(0, 0, proyv_u[0], proyv_u[1], angles="xy", scale_units="xy", scale=1, color="blue", label="u")
    plt.quiver(0, 0, proyv_u2[0], proyv_u2[1], angles="xy", scale_units="xy", scale=1, color="red", label="u2")

    #modifica el plano donde se grafica
    plt.axhline(0, color="black", lw=0.5) #dibuja la linea en y = 0 y da su color y grosor
    plt.axvline(0, color="black", lw=0.5) #dibujar la linea en x = 0 y da su color y grosor
    plt.grid() #dibuja la cuadricula
    plt.gca().set_aspect("equal") #hace que las xs y las ys sean proporcionales

    #limita la cuadricula
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)

    #le da un titulitos uwuwu
    plt.title("Vector y sus proyecciones")
    plt.legend()

    #lo muestra pois
    plt.show()