# Writing The Logic without implementation on GUI (PyGame)
from strategy import strategies, Strategy, score
import typing

flag = [True for _ in range(len(strategies))]

needed_strategies = []

for i in range(len(strategies)):
    if flag[i]:
        needed_strategies.append(strategies[i])

def tournament_logic(strategies: typing.List[Strategy],rounds) -> typing.List[list]:
    prev_results = []
    scores = []

    for index, strategy in enumerate(strategies):
        scoree = [0,0,0,0,0]

        for opponent_strategy in strategies:
            for _ in range(rounds):
                self_choice = strategy.giveNextChoice(
                    prev_results=prev_results,place=0
                    )
                opp_choice = opponent_strategy.giveNextChoice(
                    prev_results=prev_results,place=1
                    )

                prev_results.append((self_choice,opp_choice))

                curr_score = score((self_choice,opp_choice),0)
                if curr_score == 5:
                    scoree[4] += 1
                
                elif curr_score == 3:
                    scoree[3] += 1
                
                elif curr_score == 1:
                    scoree[2] += 1
                
                else:
                    scoree[1] += 1

                scoree[0] += curr_score

            prev_results = []
            
        scores.append(scoree)
    
    return scores

if __name__ == '__main__':
    rounds = 200
    results = tournament_logic(needed_strategies,rounds)
    print(results)
    
    winner = ""
    winner_pts = []

    for i in range(len(strategies)):
        if results[i] > winner_pts:
            winner_pts = results[i]
            winner = strategies[i]

        print(f"{strategies[i].name} - {results[i]}")
    
    print("----------------------------------------------------------")
    print("WINNER:",winner.name)
    print("WINNER TYPE:",winner.strategy_type)
    print(f"POINTS: {winner_pts}/{rounds*len(strategies)*5}") 