
from M1_Actividad.ModelCleaner import ModelCleaner
import time

def cleaner_robot_activity():

    # cantidad de agentes
    # dimension de matriz
    # dimension de matriz
    # porcentaje de celdas sucias
    model = ModelCleaner(4, 6, 6, 0.20)

    # cantidad de steps (maximo tiempo de ejecucion)
    max_exec_time = 15

    model.initial_time = time.time()

    # cantidad de set
    for i in range(max_exec_time):
        model.step()
        print('porcentaje de limpieza:', str(round(model.dirtyCellRatio() * 100, 2)) + '%')

    print(model.total_movements())

    model.final_time = time.time()

    model.program_execution_time()