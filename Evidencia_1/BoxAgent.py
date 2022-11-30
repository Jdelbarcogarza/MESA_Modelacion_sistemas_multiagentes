import mesa
import math

class taken():
    def __init__(self):
        self.taken = True


class BoxAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.carrying = 0
        self.stackCount = 0
        self.tempClosest = 100
        self.point = 0
        self.movingToX = 0
        self.movingToY = 0

    def step(self):
        if (self.carrying == 0):

            for i in range(len(self.model.boxCoords)):

                if((math.dist(self.pos, self.model.boxCoords[i])) < self.tempClosest):
                    print(self.tempClosest)
                    self.tempClosest = math.dist(self.pos, self.model.boxCoords[i])

                    #if(self.model.grid.is_cell_empty(self.pos) == False):

                    self.point = self.model.boxCoords[i]
                self.movingToX = self.point[0]
                self.movingToY = self.point[1]

        #place a object in pos with box next agent checks coords of box if it detects object skip to next
        
        self.move()

    def move(self):

        if(self.carrying == 0):

            if(self.pos[0] != self.movingToX):

                if(self.pos[0] <= self.movingToX):
                    new_pos = (self.pos[0] + 1, self.pos[1])

                else:

                    new_pos = (self.pos[0] - 1, self.pos[1])

            if(self.pos[1] != self.movingToY):

                if(self.pos[1] <= self.movingToY):

                    new_pos = (self.pos[0], self.pos[1] + 1)

                else:

                    new_pos = (self.pos[0], self.pos[1] + -1)

            if(self.pos[1] == self.movingToY and self.pos[0] == self.movingToX):
                self.carrying += 1
                self.pickUp()

        if(self.carrying == 1):

            if(self.pos[0] != 0):

                if(self.pos[0] <= self.movingToX):

                    new_pos = (self.pos[0] - 1, self.pos[1])

            else:

                if(self.pos[1] != 0):

                    new_pos = (self.pos[0], self.pos[1] - 1)

            #if(len(self.get_neighborhood(self.pos, moore = False, include_center = True, radius = 0)) == 0):
                        #new_pos = (self.pos[0], self.pos[1] + 1)

        self.model.grid.move_agent(self,new_pos)


    def pickUp(self):
        if(self.carrying == 0):
            print()

    def dropOff(self):
        carrrying -= 1

