import mesa


class CarAgent(mesa.Agent):

    def __init__(self, unique_id, model):

        # heredar todos los métodos y tributos de la clase pade.
        super().__init__(unique_id, model)
