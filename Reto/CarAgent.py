import mesa


class CarAgent(mesa.Agent):

    def __init__(self, unique_id, model):

        # heredar todos los métodos y tributos de la clase pade.
        super().__init__(unique_id, model)

    def move(self):

        # coordenadas actuales del agente
        row, col = self.pos
        print('analizando agente en', self.pos)

        # mover los agentes de flujo continuo en carril 0
        if row == 0:

            # poner simbolo de calle
            self.model.space_matrix[row][col] = '_'

            # mover agente 1 casilla a la derecha en grid de modelo
            self.model.grid.move_agent(self, (0, self.pos[1] + 1))

            row, col = self.pos
            # colocar simbolo de Carro en matriz impresa
            self.model.space_matrix[row][col] = 'C'

        # agentes de carril 1
        elif row == 1:

            # checar si hay carro adelante para moverse
            surroundings = self.model.grid.get_neighborhood(
                self.pos,
                moore=True,
                include_center=False
            )

            print(surroundings)

            # CASO LIMITE EN ULTIMA COLUMNA 8 o EN EL INICIO COLUMNA 0
            if col == 8 or col == 0:

                # Si casilla esta libre, mover al agente
                if type(self.model.grid[surroundings[3]]) != CarAgent:

                    # modificar matriz impresa
                    self.model.space_matrix[row][col] = '_'

                    # mover agente
                    self.model.grid.move_agent(self, (1, col + 1))

                    row, col = self.pos
                    # colocar simbolo de Carro en matriz impresa
                    self.model.space_matrix[row][col] = 'C'

                # si hay un carro parado adelante, no nos podremos mover
                elif type(self.model.grid[surroundings[3]]) == CarAgent:
                    print('no me muevo. Tengo coche adelante PARADO. Soy:', self.unique_id, self.pos)

                    pass

            # checar si tienes un carro enfrente en medio de la matriz
            elif type(self.model.grid[surroundings[4]]) == CarAgent:
                print('carro parado enfrente. No me muevo', self.unique_id, self.pos)

            # checar si agente esta donde debe pararse con el semaforo de main street
            elif self.pos == (1, 3):

                # si el semaforo main st. esta en verde, avanzan los carros
                if self.model.grid[2][3].is_green:

                    # modificar matriz impresa
                    self.model.space_matrix[row][col] = '_'

                    # mover agente
                    self.model.grid.move_agent(self, (1, col + 1))

                    row, col = self.pos
                    # colocar simbolo de Carro en matriz impresa
                    self.model.space_matrix[row][col] = 'C'

                    # si el semaforo esta en rojo
                else:
                    print('semaforo main st. en rojo no me muevo', self.unique_id, self.pos)

            # los autos se mueven normal hacia la derecha
            else:

                # modificar matriz impresa
                self.model.space_matrix[row][col] = '_'

                # mover agente
                self.model.grid.move_agent(self, (1, col + 1))

                row, col = self.pos
                # colocar simbolo de Carro en matriz impresa
                self.model.space_matrix[row][col] = 'C'


    def get_agent_pos(self):

        # retorna una tupla
        return self.pos


    def step(self):
        self.move()

