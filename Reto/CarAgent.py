import mesa


class CarAgent(mesa.Agent):

    def __init__(self, unique_id, model):

        # heredar todos los métodos y tributos de la clase pade.
        super().__init__(unique_id, model)

    def move(self):

        # coordenadas actuales del agente
        row, col = self.pos

        # mover los agentes de flujo continuo en carril 0
        if row == 0:

            # mover en matriz impresa

            # poner simbolo de calle
            self.model.space_matrix[row][col] = '_'

            # mover agente 1 casilla a la derecha en grid de modelo
            self.model.grid.move_agent(self, (0, self.pos[1] + 1))
            print('soy agente: ', self.unique_id, 'ando en ', self.pos)

            row, col = self.pos
            # colocar simbolo de Carro en matriz impresa
            self.model.space_matrix[row][col] = 'C'

        # agentes de carril 1
        elif row == 1:

            # checar si hay carro adelante para moverse
            surroundings = self.mode.grid.get_neighborhood(
                self.pos,
                moore=True,
                include_center=False
            )

            print('alrededor', surroundings)

            # checar si esta en la casilla de semaforo



            pass

    def get_agent_pos(self):

        # retorna una tupla
        return self.pos

    def step(self):
        self.move()

