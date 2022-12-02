import mesa


class RobotAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.carryingBox = False


    # metodo para buscar la caja objetivo para que el robot se mueva hacia ella.
    def searchTargetBox(self):
        pass

    def step(self):
        pass
        # llamar a move

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )

        new_pos = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_pos)


    



