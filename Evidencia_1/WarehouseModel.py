import mesa
from Evidencia_1.BoxRobotAgent import BoxAgent


class BoxModel(mesa.Model):

    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)

        # Matriz para representar el espacio
        self.space_matrix = [['_' for _ in range(width)] for _ in range(height)]


        # Create agents
        for i in range(self.num_agents):
            a = BoxAgent(i, self)
            self.schedule.add(a)

            # colocar agentes de manera aleatoria en el grid.
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

            # colocar en matriz de espacio agentes
            self.space_matrix[x][y] = 'R'

        self.print_space_matrix()


    def step(self):
        self.schedule.step()


    def print_space_matrix(self):
        # imprimir matriz
        for row in self.space_matrix:
            print(row)
