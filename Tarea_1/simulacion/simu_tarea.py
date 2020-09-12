#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OBSERVACIONES: Esta animación es para evaluar a la funcion obtenida en el punto dos
solo modificando la velocidad a partir de un valor de K dado. 
Los datos que se usan como valores fijos son random, es decir, solo se utilizan como
fijos para conocer un valor de K particular para el caso de dichos casos fijados. 

Mas adelante voy a modificarlo para que los valores de R, D y H tengan sus Slaiders con 
las condiciones planteadas en el problema
"""
######################################################################
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
######################################################################

###################################
# Objeto figura y caracteristicas #
###################################
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

#############
# Variables #
#############
π = np.pi
g = 9.81 # in m . s^2
k = 2 # in m . s^3
H = 200 # in m
L = 300 # in m
v0 = 40
delta_v0 = 0.1
t0 = 0
α0 = π/3 # in rad
R = 50
npoints = 2000
T = 10
dt = T/npoints

##############
# Ecuaciones #
##############

# Posicion del proyectil
x_p = np.linspace( 0 , 2 * L, npoints)
y_0 =  (3 ** (1/2)) * R
y_p = y_0 + np.tan(α0) * x_p - (g/2) * ((x_p)**2)/(v0)**2 * (1 + (np.tan(α0)) **2) 

##############################
# Posicion del Punto deseado #
##############################
x_h = L * np.ones(npoints)
y_h = np.linspace(0, H, npoints)

############
# Ploteos  # 
############
ax.plot(x_h, y_h, '--')
plt.scatter(L, H, marker='$P$', color='k', s=100)

###########
# Punto 2 #
###########
# flecha
# x_flecha = R * np.cos(α0)
y_flecha = 50 + 50 * np.sin(α0)
plt.scatter(0, y_flecha , marker='o', color='Black', s=100)
plt.scatter(0 - 20, y_flecha, marker='$(2)$', color='Black', s=100)
a = ax.annotate("", xy=( v0 * np.cos(α0), y_flecha + v0 * np.sin(α0)), xytext=(0, y_flecha),
                arrowprops=dict(arrowstyle="->"))

###########
# Punto 3 #
###########
plt.scatter(40, 100, marker='$(3)$', color='Black', s=100)


#################
# Delimitadores #
#################
ax.set_xlim([0, L * 1.2])
ax.set_ylim([0, H * 1.2])
l, = plt.plot(x_p, y_p, lw=2)
ax.margins(x=0)

##############################
# Slider para EL valor de K  #
##############################
axcolor = 'lightgoldenrodyellow'
axv0 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
K = Slider(axv0, 'K [cte]', 0.1, 5.0, valinit=1, valstep=.01)

def update(val):
    v0 =  (2/3) * R * ((π) ** (1/2)) * K.val

    l.set_ydata(y_0 + np.tan(α0) * x_p - (g/2) * ((x_p)**2)/(v0)**2 * (1 + (np.tan(α0)) **2))
    
    fig.canvas.draw_idle()

K.on_changed(update)

##################
# Boton de reset #
##################
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    K.reset()
    alphas.reset()
button.on_clicked(reset)

######################
# Dibujar un circulo #
######################
ax.set_aspect(1)
ax.add_artist(plt.Circle((38, 50), 50, fill=False))

plt.show()