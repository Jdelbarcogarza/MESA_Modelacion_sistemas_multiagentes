import mesa


class CarAgent(mesa.Agent):

    def __init__(self, unique_id, model):

        # heredar todos los métodos y tributos de la clase pade.
        super().__init__(unique_id, model)

        self.sub_st_car = False

        # verificar si no es un carro que esta Sub st. Si sí lo está, entonces darle un atributo especial
        # para hacer que reaparezca en Sub st. una vez termine su ruta por Main st.
        '''
        row, col = self.pos
        
        if row >= 2 and col == 4:
            self.sub_st_car = True
        '''

    def move(self):

        # coordenadas actuales del agente
        row, col = self.pos
        print('analizando agente en', self.pos)

        # mover los agentes de flujo continuo en carril 0
        if row == 0:

            self.update_output_matrix(row, col)

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

                    self.update_output_matrix(row, col)

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

                    self.update_output_matrix(row, col)

                    # si el semaforo esta en rojo
                else:
                    print('semaforo main st. en rojo no me muevo', self.unique_id, self.pos)

            # los autos se mueven normal hacia la derecha
            else:

                self.update_output_matrix(row, col)

    # el parametro de 'row' indica por qué fila debe moverse el carro.
    # los parametros provienen de la funcion move().
    # esto es una helper function para simplificar codigo
    def update_output_matrix(self, row, col):

        # modificar matriz impresa
        self.model.space_matrix[row][col] = '_'

        # mover agente
        self.model.grid.move_agent(self, (row, col + 1))

        row, col = self.pos
        # colocar simbolo de Carro en matriz impresa
        self.model.space_matrix[row][col] = 'C'

    def get_agent_pos(self):

        # retorna una tupla
        return self.pos


    def step(self):
        self.move()

