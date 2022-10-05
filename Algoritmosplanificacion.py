import operator
class Algoritmosplanificacion:
    def __init__(self):
        self.datos = []
        self.numeroProcesos = 0
        self.prioridad_proceso = []

    def getDatos(self):
        self.numeroProcesos = input("Ingrese número de procesos: ")
        for i in range(int(self.numeroProcesos)):
            temp_tiempo = int(input("Ingrese tiempo para el proceso #" + str(i + 1) + ": "))
            temp_prioridad = int(input("Ingrese la prioriodad del proceso #" + str(i + 1) + ": "))
            self.datos.append(temp_tiempo)
            self.prioridad_proceso.append(temp_prioridad)

    def Fcfs(self):
        tiempoTotalEspera = 0.0
        tiempoTotalPromedioRetorno = 0.0
        tiempoEspera = [0]
        D = list(self.datos)
        for i in range(1, int(self.numeroProcesos)):
            temp = int(D[i - 1]) + int(tiempoEspera[i - 1])
            tiempoEspera.append(temp)
        for i in range(0, int(self.numeroProcesos)):
            tiempoTotalEspera = tiempoTotalEspera + tiempoEspera[i]
        for i in range(0, int(self.numeroProcesos)):
            tiempoTotalPromedioRetorno = tiempoTotalPromedioRetorno + tiempoEspera[i] + int(D[i])

        print("| Promedio tiempo de espera: " + str(round(tiempoTotalEspera / int(self.numeroProcesos), 2)) + "  |")
        print("| Promedio tiempo de retorno: " + str(round(int(tiempoTotalPromedioRetorno) / int(self.numeroProcesos), 2)) + "|")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def Sjf(self):
        tiempoTotalEspera = 0.0
        tiempoTotalPromedioRetorno = 0.0
        tiempoEspera = [0]

        min_list = self.datos.index(min(self.datos))
        datos_reorganizados = list(self.datos)
        datos_reorganizados.pop(min_list)
        datos_reorganizados.insert(0, min_list)
        for i in range(1, int(self.numeroProcesos)):
            temp = int(datos_reorganizados[i - 1]) + int(tiempoEspera[i - 1])
            tiempoEspera.append(temp)
        for i in range(0, int(self.numeroProcesos)):
            tiempoTotalEspera = tiempoTotalEspera + tiempoEspera[i]
        for i in range(0, int(self.numeroProcesos)):
            tiempoTotalPromedioRetorno = tiempoTotalPromedioRetorno + tiempoEspera[i] + int(datos_reorganizados[i])

        # print(reorganizacion)
        print("| Promedio tiempo de espera: " + str(round(tiempoTotalEspera / int(self.numeroProcesos), 2)) + "  |")
        print("| Promedio tiempo de retorno: " + str(round(int(tiempoTotalPromedioRetorno) / int(self.numeroProcesos), 2)) + " |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def Prioridad(self):
        tiempoTotalEspera = 0.0
        tiempoTotalPromedioRetorno = 0.0
        tiempoEspera = [0]

        #D = list(self.datos)
        #Creo un diccionario con el tiempo de proceso y la prioridad  {proceso:prioridad}
        diccionario_datos_prioridad = dict(zip(self.datos, self.prioridad_proceso))
        #Ordeno el diccionario por prioridades
        diccionario_ordenado = dict(sorted(diccionario_datos_prioridad.items(), key=operator.itemgetter(1)))

        #Obtengo las keys = tiempo de espera de los procesos ya ordenados por prioridad
        lista_timpo_prioridad = diccionario_ordenado.keys()
        lista_timpo_prioridad = list(lista_timpo_prioridad)


        for i in range(1, int(self.numeroProcesos)):
            temp = int(lista_timpo_prioridad[i - 1]) + int(tiempoEspera[i - 1])
            tiempoEspera.append(temp)
        for i in range(0, int(self.numeroProcesos)):
            tiempoTotalEspera = tiempoTotalEspera + tiempoEspera[i]
        for i in range(0, int(self.numeroProcesos)):
            tiempoTotalPromedioRetorno = tiempoTotalPromedioRetorno + tiempoEspera[i] + int(lista_timpo_prioridad[i])

            # print(reorganizacion)
        print("| Promedio tiempo de espera: " + str(round(tiempoTotalEspera / int(self.numeroProcesos), 2)) + "  |")
        print("| Promedio tiempo de retorno: " + str(round(int(tiempoTotalPromedioRetorno) / int(self.numeroProcesos), 2)) + " |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



