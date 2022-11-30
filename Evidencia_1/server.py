from WarehouseModel import cleaningModel
from RobotAgent import cleaningAgent
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

numCells = 20
sizeOfCanvasX = 720
sizeOfCanvasY = 500

simParams = {
    "NumberOfAgents": UserSettableParameter(
        "slider",
        "Number of Agents",
        10,  # default
        1,  # min
        20,  # max
        1,  # step
        description="Number of agents",
    ),

    "width": numCells,
    "height": numCells,
}


def agentPortrayal(agent):
    portrayal = {"Shape": "Circle", "Filled": "true", "r": 0.5}

    if agent.state == 1:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
    return portrayal


grid = CanvasGrid(agentPortrayal, numCells, numCells,
                  sizeOfCanvasX, sizeOfCanvasY)
server = ModularServer(cleaningModel, [grid], "Cleaning Model", simParams)
server.port = 8521
server.launch()
