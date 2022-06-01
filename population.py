class Population:
    def __init__(self, generation, fixed_transfers, target_state):
        self.generation = generation
        self.rate_list = []
        self.fixed_transfers = fixed_transfers
        self.target_state = target_state

    def calculate_rates(self, starting_state, possible_transfers):
        rates_list = []
        for j in range(len(self.fixed_transfers)):
            transfer_rates_list = []
            for solution in self.generation:
                diff = []
                starting_state = 40
                for i in range(len(solution)):
                    if possible_transfers[j][1] == j:
                        starting_state = starting_state - solution[i]
                    elif possible_transfers[j][2] == j:
                        starting_state = starting_state + solution[i]
                    starting_state = starting_state + self.fixed_transfers[j][i]
                    diff.append(starting_state)
                transfer_rates_list.append(diff)
            rates_list.append(transfer_rates_list)
        print(rates_list)

        for i in range(len(self.generation)):
            for j in range(len(rates_list)):
                print(rates_list[j][i])







