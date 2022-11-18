import mesa
import math

from Reto.CarAgent import CarAgent
from Reto.TrafficLightAgent import TrafficLightAgent


class StreetModel(mesa.Model):

    def __init__(self, number_of_agents, height, width):

        self.num_agents = number_of_agents + 2  # se suman 2 por los dos semaforos en el espacio
        self.grid = mesa.space.SingleGrid(height, width, True)
        self.schedule = mesa.time.BaseScheduler(self)

        # Matriz para representar el espacio
        self.space_matrix = [[0 for _ in range(height)] for _ in range(width)]

        # ------------ insertamos semáforos -------------

        # CALLE PRINCIPAL. Se construye agente
        main_street_traffic_light = TrafficLightAgent(20, self)

        # se agrega agente en el grid
        self.grid.place_agent(main_street_traffic_light, (2, 3))
        pos_x, pos_y = main_street_traffic_light.get_position()

        # se agrega agente de semaforo PRINCIPAL al modelo
        self.schedule.add(main_street_traffic_light)

        # se agrega en nuestra matriz
        self.space_matrix[pos_x][pos_y] = main_street_traffic_light.name_id

        # CALLE SECUNDARIA. Se construye agente
        sub_street_traffic_light = TrafficLightAgent(30, self)

        # se agrega agente de semaforo SECUNDARIO al modelo
        self.schedule.add(sub_street_traffic_light)

        # poner este semaforo en rojo
        sub_street_traffic_light.change_light()

        self.grid.place_agent(sub_street_traffic_light, (2, 5))
        pos_x, pos_y = sub_street_traffic_light.get_position()

        self.space_matrix[pos_x][pos_y] = sub_street_traffic_light.name_id

        # crear agentes y asignarlos al modelo
        for i in range(number_of_agents):
            a = CarAgent(i, self)

            # se carga agente al modelo
            self.schedule.add(a)

        # carros en trafico continuo
        self.grid.place_agent(CarAgent(1, self), (0, 0))
        self.space_matrix[0][0] = 'C'

        self.grid.place_agent(CarAgent(2, self), (0, 3))
        self.space_matrix[0][3] = 'C'

        self.grid.place_agent(CarAgent(3, self), (0, 5))
        self.space_matrix[0][5] = 'C'

        self.grid.place_agent(CarAgent(4, self), (1, 3))  # main_street car
        self.space_matrix[1][3] = 'C'

        self.grid.place_agent(CarAgent(5, self), (2, 4))  # sub_street car
        self.space_matrix[2][4] = 'C'

        self.grid.place_agent(CarAgent(6, self), (1, 1))  # main
        self.space_matrix[1][1] = 'C'

        self.grid.place_agent(CarAgent(8, self), (3, 4))  # sub
        self.space_matrix[3][4] = 'C'

        self.grid.place_agent(CarAgent(8, self), (1, 0))  # main
        self.space_matrix[1][0] = 'C'

        self.grid.place_agent(CarAgent(7, self), (5, 4))  # sub
        self.space_matrix[5][4] = 'C'

        self.grid.place_agent(CarAgent(7, self), (1, 6))  # main
        self.space_matrix[1][6] = 'C'

        # Agregar zona muerta
        for row in range(len(self.space_matrix)):
            for col in range(len(self.space_matrix)):
                if self.space_matrix[row][col] == 0:
                    self.space_matrix[row][col] = 'x'

        # imprimir matriz
        for row in self.space_matrix:
            print(row)

    def step(self):
        pass