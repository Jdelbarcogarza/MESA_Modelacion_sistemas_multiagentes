import mesa


class CarAgent(mesa.Agent):

    def __init__(self, unique_id, model):

        # heredar todos los métodos y tributos de la clase pade.
        super().__init__(unique_id, model)

        # es un agente originario de sub st. ?
        self.sub_st_car = False

    # verificar si no es un carro que esta Sub st. Si sí lo está, entonces darle un atributo especial
    # para hacer que reaparezca en Sub st. una vez termine su ruta por Main st.
    def define_agent_street_status(self):

        row, col = self.pos

        if row >= 2 and col == 4:
            self.sub_st_car = True

    def move(self):

        # coordenadas actuales del agente
        row, col = self.pos
        # print('analizando agente en', self.pos) # DEBUG PRINT

        # obtener alrededores del agente
        surroundings = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )

        # mover los agentes de flujo continuo en carril 0 (Main st.)
        if row == 0:

            self.update_output_matrix(row, col)

        # agentes de carril 1 (Main st.)
        elif row == 1:

            # print(surroundings) # DEBUG PRINT

            # CASO LIMITE EN ULTIMA COLUMNA 8 o EN EL INICIO COLUMNA 0
            if col == 8 or col == 0:

                # carro normal de main st. continua por la avenida si llega al final de la misma
                if not self.sub_st_car:
                    # Si casilla esta libre, mover al agente
                    if type(self.model.grid[surroundings[3]]) != CarAgent:

                        self.update_output_matrix(row, col)

                    # si hay un carro parado adelante, no nos podremos mover
                    elif type(self.model.grid[surroundings[3]]) == CarAgent:
                        # DEBUG PRINT
                        # print('no me muevo. Tengo coche adelante PARADO. Soy:', self.unique_id, self.pos)
                        pass

                elif col == 8 and self.sub_st_car:

                    # actualizar matrix de espacio
                    self.model.space_matrix[row][col] = '_'

                    # entrada de sub st.
                    self.model.space_matrix[8][4] = 'C'

                    # verificar espacio disponible en casilla entrante de sub st.
                    if self.model.grid.is_cell_empty((8, 4)):
                        self.model.grid.move_agent(self, (8, 4))
                    else:
                        # print('entrada a sub st. ocuapada', self.pos, 'soy', self.unique_id)  # DEBUG PRINT
                        pass

            # checar si tienes un carro enfrente en medio de la matriz
            elif type(self.model.grid[surroundings[4]]) == CarAgent:
                # print('carro parado enfrente. No me muevo', self.unique_id, self.pos) # DEBUG PRINT
                pass

            # checar si agente esta donde debe pararse con el semaforo de main street
            elif self.pos == (1, 3):

                # si el semaforo main st. esta en verde, avanzan los carros
                if self.model.grid[2][3].is_green:

                    self.update_output_matrix(row, col)

                    # si el semaforo esta en rojo
                else:
                    # print('semaforo main st. en rojo no me muevo', self.unique_id, self.pos)  # DEBUG PRINT
                    pass
            # los autos se mueven normal hacia la derecha
            else:

                self.update_output_matrix(row, col)

        # movimiento de agente en calle secundaria (Sub st.)
        elif row >= 2:

            # print(surroundings) # DEBUG PRINT

            # verificar si hay auto en frente
            if type(self.model.grid[surroundings[1]]) == CarAgent:

                # print('no avanzo, tengo carro enfrente', self.pos, 'soy', self.unique_id)  # DEBUG PRINT
                pass

            # si estas en casilla para semaforo
            elif self.pos == (2, 4):

                # si semaforo esta verde
                if self.model.grid[2][5].is_green:

                    self.model.space_matrix[row][col] = '_'

                    # incorporar a main st. al agente
                    self.model.grid.move_agent(self, (row - 1, col))

                    row, col = self.pos

                    self.model.space_matrix[row][col] = 'C'

                # si semaforo esta en rojo
                else:

                    # DEBUG PRINT
                    # print('semaforo en sub st. en ROJO. No me puedo mover', self.pos, 'soy', self.unique_id)
                    pass

            # mover al agente por sub st.
            else:

                self.model.space_matrix[row][col] = '_'

                # i
                self.model.grid.move_agent(self, (row - 1, col))

                row, col = self.pos

                self.model.space_matrix[row][col] = 'C'

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

