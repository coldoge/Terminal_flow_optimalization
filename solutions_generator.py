import random


def create_first_generation(number_of_solutions, possible_transfers):
    generation = []
    for i in range(0, number_of_solutions):
        solution = []
        for transfer in possible_transfers:
            solution.append(random.randint(0, transfer[0]))
        generation.append(solution)
    return generation
