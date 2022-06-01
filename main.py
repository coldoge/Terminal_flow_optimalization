import random
from population import Population
from solutions_generator import create_first_generation

possible_transfers = [[10, 0, 1], [12, 0, 1], [8, 1, 0]]
number_of_solutions = 10
fixed_transfers = [[5, -3, 14], [-3, -2, -3]]


new_generation = Population(create_first_generation(number_of_solutions, possible_transfers), fixed_transfers, 40)
print(new_generation.generation)
new_generation.calculate_rates(40, possible_transfers)