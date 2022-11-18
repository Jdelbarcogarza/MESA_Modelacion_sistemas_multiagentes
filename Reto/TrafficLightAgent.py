import mesa

# clase de semaforo para controlar flujo de tráfico
class TrafficLight(mesa.Agent):

    def __init__(self, unique_id, model, is_green, position_x, position_y):

        super().__init__(unique_id, model, is_green, position_x, position_y)

        self.name_id = 'TF'  # id para identificar en la matriz de espacio
        self.is_green = is_green  # boolean

        # row
        self.position_x = position_x  # int

        # column
        self.position_y = position_y  # int

    def get_position(self):
        return [self.position_x, self.position_y]

    def get_is_green(self):
        return self.is_green

    def change_light(self):
        self.is_green = not self.is_green
