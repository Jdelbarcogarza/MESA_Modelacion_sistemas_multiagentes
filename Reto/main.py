
from Reto.StreetModel import StreetModel

def modelo_de_reto():

    # construir modelo
    model = StreetModel()

    step_amount = 15

    for i in range(step_amount):
        model.step()

    print('num of ag', model.num_agents)

# en cada GET del cliente, debo correr un step
