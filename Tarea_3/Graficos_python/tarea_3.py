"""
        "SIMULACION" DE LOS PUNTOS DE EQUILIBRIO EJERCICIO :

        Lo que hacemos aca es plantear las posiciones de equilibrio animando un grafico 
    para cada variable presente en la ecuacion de equilibrio. 
        Las variables que variamos son: k, R, m y M. 
        Por otro lado, tambien dejamos varios grafiCos con casos fijos para visualizar 
    como varia respecto de un valor concreto los graficos presentes. Estos se pueden
    comentar, si se quiere para dejar de visualizarlos mientras variamos la recta sobre 
    el seno.
"""
######################################################################
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
import matplotlib.ticker as ticker
######################################################################

###############################################
# Variables inicializados en valores iniciales#
###############################################
cord = np.arange(-4, 4, 0.01)
π    = np.pi
φ    = np.arange((-1) * (π/2), (π/2), 0.01)
g    = 9.81  
M    = 300    
m    = 200    
k    = 10     
φ0   = π/3  
R    = 500   
om   = (k * R)/(m * g)
om_2 = (k * R)/(m+100 * g)

##################################
#    Ecuaciones para graficar    #
##################################
# Seno 
f_φ = np.sin(φ)
h_φ = np.cos(φ)

# Rectas 
g_φ   = (-om * φ) + M/m 
g_φ_1 = (-om * φ) + (M+100)/m 
g_φ_2 = (-om_2 * φ) + M/(m+100) 

#################
#     Ploteo    #
#################
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3, bottom=0.3)

# Ejes Coordenados
ax.plot( cord   , cord*0 , color='black') 
ax.plot( cord*0 , cord   , color='black')
# Funciones
ax.plot( φ,   f_φ) # Soy la funcion seno, si no me queres ver comentame
ax.plot( φ,   h_φ) # Soy la funcion coseno, si no me queres ver comentame
ax.text(1,  1.1 , r'$\sin{(\varphi)}$', fontsize=10) # Soy el texto seno que aparece en el grafico, si no me queres ver comentame
ax.text(1, -0.3 , r'$\cos{(\varphi)}$', fontsize=10) # Soy el texto coseno que aparece en el grafico, si no me queres ver comentame
ax.plot( φ,   g_φ, color =  'red')  # Soy la recta con ordenada M/m, si no me queres ver comentame 
ax.plot( φ, g_φ_1, color =   'red') # Soy la recta con ordenada M+100/m, si no me queres ver comentame
ax.plot( φ, g_φ_2, color = 'green') # Soy la recta con ordenada M/m+100, si no me queres ver comentame

# Ordenadas (Si no me quieren ver comenten estas 6 lineas)
ax.scatter( 0,       M/m, color='black') 
ax.scatter( 0, (M+100)/m, color='black')
ax.scatter( 0, M/(m+100), color='black')
ax.annotate(    r'$\frac{M}{m}$', xy=( 0,       M/m ), xytext=( -0.3,      M/m  ), arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
ax.annotate(r'$\frac{M+100}{m}$', xy=( 0, (M+100)/m ), xytext=( 0.2, ( M+100)/m ), arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
ax.annotate(r'$\frac{M}{m+100}$', xy=( 0, M/(m+100) ), xytext=( -0.4, M/(m+100) ), arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))

# Puntos de equilibrio en graficos fijos (Si no me quieren ver comenten estas 3 lineas)
ax.scatter( 0.42,  0.4, label=r'$\varphi_{eq(1}$', color = 'cyan')
ax.scatter( 0.55, 0.55, label=r'$\varphi_{eq(2}$', color =  'red')
ax.scatter(  0.2,  0.2, label=r'$\varphi_{eq(3}$', color ='green')

"""
De aca para abajo NO COMENTAR NADA
"""

# Seteo valores de las coordenadas
ax.set(
       xlabel = r'${\varphi}_{eq}$', 
       ylabel = r'$\sin{({\varphi}_{eq})}$',
       title  = 'Interseccion de las Graficas de la ecuacion (8)'
       )
x = np.arange(-10,10.5,.5)       

# Para cambiar la vista de los valores en la coordenada x y ponerlo en valores de π
positions = [-π/2, -π/4 , 0 , π/4, π/2]
labels = [ r'$-\frac{\pi}{2}$', r'$-\frac{\pi}{4}$','0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$']
ax.xaxis.set_major_locator(ticker.FixedLocator(positions))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels))

ax.grid()

#################
# Delimitadores #
#################
ax.set_xlim([ -(π/2),  π/2])
ax.set_ylim([     -4,    4])
l, = plt.plot(φ, g_φ, lw=2)
ax.margins(x=0)

##############################
# Slider para EL valor de K  #
##############################
axcolor = 'lightgoldenrodyellow'
#               [pos_x,pos_y,largo,ancho]                      
ax_m = plt.axes([  0.6, 0.15,  0.3, 0.02], facecolor=axcolor)
ax_M = plt.axes([  0.2, 0.05,  0.3, 0.02], facecolor=axcolor)
ax_R = plt.axes([  0.2,  0.1,  0.3, 0.02], facecolor=axcolor)
ax_k = plt.axes([  0.2, 0.15,  0.3, 0.02], facecolor=axcolor)

n_m = Slider(ax_m, 'm [cte]', 0.1, 1000.0, valinit=1, valstep=.01)
n_M = Slider(ax_M, 'M [cte]', 0.1, 1000.0, valinit=1, valstep=.01)
n_R = Slider(ax_R, 'R [cte]', 0.1, 1000.0, valinit=1, valstep=.01)
n_k = Slider(ax_k, 'k [cte]', 0.1, 1000.0, valinit=1, valstep=.01)

def update(val):

    M = n_M.val
    m = n_m.val
    R = n_R.val
    k = n_k.val

    l.set_ydata((-(k * R)/(m * g) * φ) + M/m)

    fig.canvas.draw_idle()

n_m.on_changed( update )
n_M.on_changed( update )
n_R.on_changed( update )
n_k.on_changed( update )


##################
# Boton de reset # 
##################
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    n_m.reset()
    n_M.reset()

button.on_clicked(reset)

ax.legend()

fig.savefig("test.png")
plt.show()