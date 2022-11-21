import mesa
import math

from Reto.CarAgent import CarAgent
from Reto.TrafficLightAgent import TrafficLightAgent


class StreetModel(mesa.Model):

    def __init__(self):

        self.num_agents = 12  # existen 12 agentes en el modelo
        self.grid = mesa.space.SingleGrid(9, 9, True)
        self.schedule = mesa.time.BaseScheduler(self)

        # Matriz para representar el espacio
        self.space_matrix = [[0 for _ in range(9)] for _ in range(9)]

        # variable de control para ver en que paso va el modelo.
        self.step_counter = 0

        # ------------ insertamos semáforos -------------

        # CALLE PRINCIPAL. Se construye agente
        main_street_traffic_light = TrafficLightAgent('Main St.', self)

        # se agrega agente en el grid
        self.grid.place_agent(main_street_traffic_light, (2, 3))
        pos_x, pos_y = main_street_traffic_light.get_position()

        # se agrega agente de semaforo PRINCIPAL al modelo
        self.schedule.add(main_street_traffic_light)

        # MODIFICAR SEMAFORO DE MAIN ST. (Cambiar a rojo)
        #main_street_traffic_light.change_light()

        # se agrega en nuestra matriz
        self.space_matrix[pos_x][pos_y] = main_street_traffic_light.name_id

        # CALLE SECUNDARIA. Se construye agente
        sub_street_traffic_light = TrafficLightAgent('Sub St.', self)

        # se agrega agente de semaforo SECUNDARIO al modelo
        self.schedule.add(sub_street_traffic_light)

        # poner este semaforo en rojo
        sub_street_traffic_light.change_light()

        self.grid.place_agent(sub_street_traffic_light, (2, 5))
        pos_x, pos_y = sub_street_traffic_light.get_position()

        self.space_matrix[pos_x][pos_y] = sub_street_traffic_light.name_id

        # coordenadas para los carros
        agent_coordinates = {
            1: (0, 0), 2: (0, 3), 3: (0, 5), 4: (1, 3),
            5: (2, 4), 6: (1, 1), 7: (3, 4), 8: (1, 0),
            9: (5, 4), 10: (1, 6)
        }

        # crear agentes y asignarlos al modelo (hay 10 autos en el modelo)
        for agent_id in agent_coordinates:

            # se construye agente
            a = CarAgent(agent_id, self)

            # se carga agente al modelo
            self.schedule.add(a)

            # se coloca en el espacio del mesa
            self.grid.place_agent(a, agent_coordinates[agent_id])

            # se coloca en matriz local de espacio
            x, y = agent_coordinates[agent_id]

            self.space_matrix[x][y] = 'C'

        # Agregar zona muerta y calle
        for row in range(len(self.space_matrix)):
            for col in range(len(self.space_matrix)):
                # agregar zona muerta. Para los dos lados de la calle
                if (row > 1 and col <= 3) and self.space_matrix[row][col] != 'T' or (row > 1 and col >= 5) and self.space_matrix[row][col] != 'T':
                    self.space_matrix[row][col] = 'x'
                elif (col == 4 or row <= 1) and self.space_matrix[row][col] == 0:
                    self.space_matrix[row][col] = '_'



    def print_space_matrix(self):
        # imprimir matriz
        for row in self.space_matrix:
            print(row)

    def step(self):

        print('iteracion: ', self.step_counter)
        self.print_space_matrix()
        self.schedule.step()

        # al final aumentar la iteracion en la que estamos
        self.step_counter = self.step_counter + 1
