# Writing The Logic without implementation on GUI (PyGame)
from strategy import strategies

flag = [True for _ in range(len(strategies))]

needed_strategies = []

for i in range(len(strategies)):
    if flag[i]:
        needed_strategies.append(strategies[i])

def tournament_logic(strategies,rounds):
    pass