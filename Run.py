from Algoritmosplanificacion import Algoritmosplanificacion
from Graficas import diagrama_gantt

class Run:

    def __init__(self):
        self.proceso = Algoritmosplanificacion()

    def inicio(self):

        print("*************************************************************")
        print("|   Bienvenido al programa de planificacion de algoritmos   |")
        print("*************************************************************")
        self.proceso.getDatos()
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|        ALGORITMO POR FCFS        |")
        self.proceso.Fcfs()
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|        ALGORITMO POR SJF         |")
        self.proceso.Sjf()
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|     ALGORITMO POR PRIORIDAD      |")
        self.proceso.Prioridad()




if __name__ == "__main__":
    Run().inicio()
