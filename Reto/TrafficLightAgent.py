import mesa

# clase de semaforo para controlar flujo de tráfico
class TrafficLightAgent(mesa.Agent):

    def __init__(self, unique_id, model):

        super().__init__(unique_id, model)

        self.name_id = 'T'  # id para identificar en la matriz de espacio
        self.is_green = True  # boolean

    def get_position(self):

        return self.pos

    def change_light(self):
        self.is_green = not self.is_green
