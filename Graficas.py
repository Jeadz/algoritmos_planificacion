from Algoritmosplanificacion import Algoritmosplanificacion
import matplotlib.pyplot as plt
import numpy as np

def diagrama_gantt():
    fig, gantt = plt.subplots()

    gantt.set_xlabel("Tiempo")
    gantt.set_ylabel("Procesos")
    lista_num_procesos = Algoritmosplanificacion
    lista_num_procesos.Fcfs()
    gantt.set_yticklabels(lista_num_procesos)
    plt.show()