import mesa

class box(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


    def get_position(self):
        return self.pos
