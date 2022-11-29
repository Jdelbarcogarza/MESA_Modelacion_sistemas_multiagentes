import mesa


class BoxAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.carrying = 0
        #self.stack
        self.stackCount = 0
    
    def step(self):
        self.move()
        if self.carrying > 0:
            self.giveBox()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore = True,
            include_center = False
        )

        new_pos = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_pos)

    def giveBox(self):
        freind = self.model.grid.get_cell_list_contents([self.pos])
        if len(freind) > 1:
            other = self.random.choice(freind)
            other.carrying += 1
            self.carrying -= 1

    



