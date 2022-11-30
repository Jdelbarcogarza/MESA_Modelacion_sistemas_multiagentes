import mesa
from Evidencia_1.RobotAgent import RobotAgent
from Evidencia_1.BoxAgent import BoxAgent


class BoxModel(mesa.Model):

    def __init__(self, N, num_boxes, width, height):
        self.num_agents = N + num_boxes
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)

        # Matriz para representar el espacio
        self.space_matrix = [['_' for _ in range(width)] for _ in range(height)]


        # Crear agentes robot
        for i in range(N):
            a = RobotAgent(i, self)
            self.schedule.add(a)

            # colocar agentes de manera aleatoria en el grid.
            x = self.random.randrange(1, self.grid.width - 1)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

            # colocar en matriz de espacio agentes
            self.space_matrix[x][y] = 'R'

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

            self.space_matrix[x][y] = 'B'

        # crear agentes de caja

        self.print_space_matrix()

            


    def step(self):
        self.schedule.step()


    def print_space_matrix(self):
        # imprimir matriz
        for row in self.space_matrix:
            print(row)
