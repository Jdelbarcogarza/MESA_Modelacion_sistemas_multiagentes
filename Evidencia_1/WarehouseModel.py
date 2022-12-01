import mesa
from Evidencia_1.RobotAgent import RobotAgent
from Evidencia_1.BoxAgent import BoxAgent
import random


class WharehouseModel(mesa.Model):

    def __init__(self, N, num_boxes, rows, cols):
        self.num_agents = N + num_boxes
        self.grid = mesa.space.MultiGrid(rows, cols, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.width = cols
        self.height = rows

        # Matriz para representar el espacio
        self.space_matrix = [['_' for _ in range(rows)] for _ in range(cols)]

        # arreglo que guarda las coordenadas de todas las cajas
        self.box_positions = []

        # Crear agentes robot
        for i in range(N):
            a = RobotAgent(i, self)
            self.schedule.add(a)

            # NOTA: randint incluye los limites
            # colocar agentes de manera aleatoria en el grid.
            row = random.randint(0, self.width - 1)  # excluimos la opción de index 10

            # evitar que salga en la primera y ultima columna un robot
            col = random.randint(1, self.height - 2)  # genera numero de 1 a 8

            print('limits', row, col)
            # colocar en matriz de espacio agentes
            self.grid.place_agent(a, (col, row))
            self.space_matrix[row][col] = 'R'

        # SETUP DE CAJAS
        for i in range(N, N + num_boxes):
            a = BoxAgent(i, self)
            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            # verificar que no se coloque la caja sobre un robot en la inicialización del modelo
            while not self.grid.is_cell_empty((x, y)):

                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)

            # se coloca el agente en una celda vacía
            self.grid.place_agent(a, (x, y))

            # agregar coordenadas arreglo de posiciones de cajas
            self.box_positions.append(tuple((x, y)))

            self.space_matrix[x][y] = 'B'


        self.print_space_matrix()
        print(self.box_positions)


    def step(self):
        self.schedule.step()


    def print_space_matrix(self):
        # imprimir matriz
        for row in self.space_matrix:
            print(row)
