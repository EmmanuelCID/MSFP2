"""
Práctica 2: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Emmanuel Cid Pacheco
Número de control: 23212187
Correo institucional: l23212187@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

# Datos de la simulación
u = np.array(pd.read_excel('signal.xlsx', header=None))
u = np.reshape(u, -1)
x0, t0, tend, dt, w, h = 0, 0, 15, 1E-3, 10, 5
N = round(tend / dt) + 1
t = np.linspace(t0, tend, N)

#Circuitos RLCZ para cada estado: [R, L, C, Z]
parametros_circuito = {
    'Normotenso': [1, 0.001, 1.500, 0.010],
    'Hipotenso':  [1, 0.001, 3.500, 0.010],
    'Hipertenso': [1, 0.001, 1.000, 0.010]
}

parametros_pid = {
    'Hipotenso':  [458.4826, 1112094.7355, 0.0062671, 1.5],
    'Hipertenso': [129.9786, 312762.8587, 0.0017461, 1.5]
}

# Componentes del circuito RLCZ y función de transferencia
def ftrans(R,L,C,Z):
    num = [L*R,R*Z]
    den = [C*L*R*Z,L*(Z+R),R*Z]
    return ctrl.tf(num, den)

# Componentes del controlador
def controlador(kP,kI,kD,Cr):
    Re = 1/(kI*Cr)
    Rr = kP*Re
    Ce = kD/Rr
    numPID = [Re*Rr*Ce*Cr,Re*Ce+Rr*Cr,1]
    denPID = [Re*Cr,0]
    return ctrl.tf(numPID, denPID)

sysN = ftrans(*parametros_circuito['Normotenso'])
sysL = ftrans(*parametros_circuito['Hipotenso'])
sysH = ftrans(*parametros_circuito['Hipertenso'])

PID_L = controlador(*parametros_pid['Hipotenso'])
PID_H = controlador(*parametros_pid['Hipertenso'])
sysPID_L = ctrl.feedback(ctrl.series(PID_L, sysL), 1, sign=-1)
sysPID_H = ctrl.feedback(ctrl.series(PID_H, sysH), 1, sign=-1)

_, PpN  = ctrl.forced_response(sysN, t, u, x0)
_, PpL  = ctrl.forced_response(sysL, t, u, x0)
_, PpH  = ctrl.forced_response(sysH, t, u, x0)
_, PIDL = ctrl.forced_response(sysPID_L, t, u, x0)
_, PIDH = ctrl.forced_response(sysPID_H, t, u, x0)

clr1 = np.array([149,100,221])/255
clr2 = np.array([255,190,145])/255
clr3 = np.array([118,196,87])/255

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'

def plotsignals(t, sig1, sig2, sig3, signal_type):
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_subplot(111)

    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.tick_params(direction='in', which='both')

    idx_markers = np.arange(0, len(t), 100)

    if signal_type == "Senal":
        ax.plot(t, sig1, '-', color=clr1, linewidth=1.5, label=r'$P_{p}(t)$: Hipotenso')
        ax.plot(t, sig2, '--', color=clr2, linewidth=1.5, markersize=5, 
                markevery=idx_markers, label=r'$P_{p}(t)$: Normotenso')
        ax.plot(t, sig3, '--', color=clr3, linewidth=1.5, markersize=5, 
                markevery=idx_markers, label=r'$P_{p}(t)$: Hipertenso')
        
    elif signal_type == "Hipotenso":
        ax.plot(t, sig1, '-', color=clr1, linewidth=1.5, label=r'$P_{p}(t)$: Hipotenso')
        ax.plot(t, sig2, '--', color=clr2, linewidth=1.5, markersize=5, 
                markevery=idx_markers, label=r'$P_{p}(t)$: Normotenso')
        ax.plot(t, sig3, '--', color=clr3, linewidth=1.5, markersize=5, 
                markevery=idx_markers, label=r'$PID(t)$: Hipotenso')
        
    elif signal_type == "Hipertenso":
        ax.plot(t, sig1, '-', color=clr1, linewidth=1.5, label=r'$P_{p}(t)$: Hipertenso')
        ax.plot(t, sig2, '--', color=clr2, linewidth=1.5, markersize=5, 
                markevery=idx_markers, label=r'$P_{p}(t)$: Normotenso')
        ax.plot(t, sig3, '--', color=clr3, linewidth=1.5, markersize=5, 
                markevery=idx_markers, label=r'$PID(t)$: Hipertenso')

    ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=3, 
              frameon=False, fontsize=9, prop={'family': 'Times New Roman', 'size': 10})
    
    ax.set_xlabel(r'$t\ [s]$', fontsize=11)
    ax.set_ylabel(r'$V_i(t)\ [V]$', fontsize=11)
    
    ax.set_xlim(0, 15)
    ax.set_xticks(np.arange(0, 16, 1))
    ax.set_ylim(-0.4, 1.2)
    ax.set_yticks(np.arange(-0.4, 1.4, 0.2))
    plt.tight_layout()
    
    filename = f"{signal_type}_python.pdf"
    fig.savefig(filename, format='pdf', bbox_inches='tight')
    print(f"Gráfica guardada exitosamente como: {filename}")
    plt.show()

if __name__ == "__main__":
    print("Ejecutando simulaciones con parámetros independientes y generando gráficos...\n")
    
    plotsignals(t, PpL, PpN, PpH, "Senal")
    plotsignals(t, PpL, PpN, PIDL, "Hipotenso")
    plotsignals(t, PpH, PpN, PIDH, "Hipertenso")