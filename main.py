# Writing The Logic without implementation on GUI (PyGame)
from strategy import strategies

flag = [True for _ in range(len(strategies))]

needed_strategies = []

for i in range(len(strategies)):
    if flag[i]:
        needed_strategies.append(strategies[i])

def tournament_logic(strategies,rounds):
    prev_results_list = [[] for _ in range(len(strategies))]

    for self_index, strategy in enumerate(strategies):
        for opp_index, opponent_strategy in enumerate(strategies):
            for round in range(rounds):
                base_string = f"ROUND-{round} --- {strategy.name} VS {opponent_strategy.name}"

                
                print(base_string)

if __name__ == '__main__':
    tournament_logic(needed_strategies,20)