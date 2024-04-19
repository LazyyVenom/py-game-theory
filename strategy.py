from typing import Callable
import random

class Strategy:
    def __init__(
        self,
        name: str,
        st_id: str,
        desc: str,
        strategy_type: str,
        logic: Callable[[list], int],
    ) -> None:
        """
        Initializes a Strategy object.

        Args:
            name (str): The name of the strategy.
            st_id (str): The ID of the strategy.
            desc (str): Description of the strategy.
            strategy_type (str): Type of the strategy.
            logic (Callable[[List[int]], int]): The function representing the logic of the strategy.
        """
        self.name = name
        self.st_id = st_id
        self.desc = desc
        self.strategy_type = strategy_type
        self.logic = logic

    def giveNextChoice(self, prev_results: list, place: int) -> int:
        """
        Calculates the next choice based on the previous results.

        Args:
            prev_results (List[list[int]]): List of previous results.

        Returns:
            int: The next choice.
            Prev_Results : [[1/0,1/0]] - [0th Strategy, 1st Strategy]
            (1 - Cooperate, 0 - Defect)
        """
        if not isinstance(prev_results, list):
            raise ValueError("prev_results must be a list")

        return self.logic(prev_results, place)


def score(results: list,place: int):
    our_choice = results[place]
    other_choice = results[int(not place)]

    # print(f"Our Choice{our_choice} Other Choice {other_choice}")

    if our_choice == other_choice == 1:
        # return "Mutual Cooperation"
        return 3

    elif our_choice == other_choice == 0:
        # return "Mutual Defection"
        return 1

    elif our_choice == 0 and other_choice == 1:
        # return "You Defect"
        return 5

    else:
        # return "They Defect"
        return 0
    

#Strategies Declared Here

def tit_for_tat_logic(prev_results,place):
    if len(prev_results) == 0:
        return 1
    
    last_result = prev_results[-1]

    return last_result[1] if place == 0 else last_result[0]


tit_for_tat = Strategy(
    name = "Tit For Tat", 
    st_id = "TFT",
    desc = "Strategy: Start with cooperation and then mirror the opponent's previous move.\nDescription: Forgiving but firm, as it retaliates against defection but forgives and returns to cooperation if the opponent cooperates again.",
    strategy_type = "NICE",
    logic = tit_for_tat_logic
)


def win_stay_lose_shift_logic(prev_results,place) -> int:
    if len(prev_results) == 0:
        return 1

    last_score = score(prev_results[-1],place)

    if last_score == 0:
        return int(not prev_results[-1][place]) 
    
    else:
        return prev_results[-1][place]


win_stay_lose_shift = Strategy(
    name = "Win Stay Lose Shift",
    st_id = "WSLS",
    desc = "Strategy: Start with cooperation. Continue cooperating as long as you win or draw; switch to defection if you lose.\nDescription: Reactive and adaptive, adjusting based on the outcome of previous interactions.",
    strategy_type = "NICE",
    logic = win_stay_lose_shift_logic
)


def pavlov_logic(prev_results,place) -> int:
    if len(prev_results) == 0:
        return 1

    last_score = score(prev_results[-1],place)

    if prev_results[-1][place] == 1:
        if last_score == 5:
            return 1
        return 0
    
    else:
        if last_score == 0:
            return 1
        else:
            return 0


pavlov = Strategy(
    name = "Pavlov",
    st_id = "PAV",
    desc = "Strategy: Start with cooperation. Keep the same action if it resulted in the highest payoff in the previous round; switch actions otherwise.\nDescription: Reinforces successful strategies while abandoning unsuccessful ones, promoting stability.",
    strategy_type = "NICE",
    logic = pavlov_logic
)


def random_logic(prev_results=[],place=0) -> int:
    return random.randint(0,1)


random_st = Strategy(
    name = "Random",
    st_id = "RAN",
    desc = "Strategy: Choose cooperation or defection randomly, with equal probability, in each round.\nDescription: Introduces unpredictability into the game, sometimes exploiting overly deterministic opponents.",
    strategy_type = "UNKNOWN",
    logic = random_logic
)


def grim_trigger_logic(prev_results,place) -> int:
    if len(prev_results) == 0:
        return 1

    for res in prev_results:
        if res[int(not place)] == 0:
            return 0
    
    return 1


grim_trigger = Strategy(
    name = "Grim Trigger",
    st_id = "GRM",
    desc = "Strategy: Start with cooperation and continue cooperating unless the opponent defects switch to defection permanently if the opponent defects.\nDescription: Punishes defection severely, promoting long-term cooperation.",
    strategy_type = "NICE",
    logic = grim_trigger_logic
)


def tit_for_2_tat_logic(prev_results,place):
    if len(prev_results) < 2:
        return 1
    
    last_result = prev_results[-1]
    sec_last_result = prev_results[-2]

    return 0 if last_result[int(not place)] == 0 and sec_last_result[int(not place)] == 0 else 1


tit_for_2_tat = Strategy(
    name = "Tit For Two Tat", 
    st_id = "TFTT",
    desc = "Strategy: Cooperate unless the opponent defects twice in a row.\nDescription: More forgiving than TFT, allowing for occasional mistakes by the opponent without triggering retaliation.",
    strategy_type = "NICE",
    logic = tit_for_2_tat_logic
)


def soft_tit_for_tat_logic(prev_results,place):
    if len(prev_results) == 0:
        return 1
    
    error_flag = 1 if random.random() > 0.8 else 0

    last_result = prev_results[-1]

    if error_flag:
        return int(not last_result[int(not place)])

    return last_result[1] if place == 0 else last_result[0]


soft_tit_for_tat = Strategy(
    name = "Soft Tit For Tat", 
    st_id = "STFT",
    desc = "Strategy: Mimic the opponent's previous move, but with a small probability of error.\nDescription: Introduces noise into the decision-making process, making it less predictable.",
    strategy_type = "NICE",
    logic = soft_tit_for_tat_logic
)


def forgiving_tit_for_tat_logic(prev_results,place):
    if len(prev_results) == 0:
        return 1
    
    forgiving_flag = 1 if random.random() > 0.8 else 0

    last_result = prev_results[-1]

    if forgiving_flag and prev_results[-1][int(not place)] == 0:
        return 1

    return last_result[1] if place == 0 else last_result[0]


forgiving_tit_for_tat = Strategy(
    name = "Forgiving Tit For Tat", 
    st_id = "FTFT",
    desc = "Strategy: Occasionally forgive the opponent's defection with immediate cooperation in return.\nDescription: Similar to TFT but with occasional unconditional cooperation, promoting flexibility.",
    strategy_type = "NICE",
    logic = forgiving_tit_for_tat_logic
)


def reverse_tit_for_tat_logic(prev_results,place):
    if len(prev_results) == 0:
        return 0
    
    last_result = prev_results[-1]

    return last_result[1] if place == 0 else last_result[0]


reverse_tit_for_tat = Strategy(
    name = "Reverse Tit For Tat", 
    st_id = "RTFT",
    desc = "Strategy: Start with defection and then mimic the opponent's previous move.\nDescription: Opposite of TFT, adjusting based on the opponent's previous move.",
    strategy_type = "NASTY",
    logic = reverse_tit_for_tat_logic
)


def cooperator_logic(prev_results,place):
    return 1


cooperator = Strategy(
    name = "Cooperator", 
    st_id = "COP",
    desc = "Strategy: Always cooperate regardless of the opponent's move.\nDescription: Maintains cooperation and can exploit opponents who defect in the long run.",
    strategy_type = "NICE",
    logic = cooperator_logic
)


def defector_logic(prev_results,place):
    return 0


defector = Strategy(
    name = "Defector", 
    st_id = "DEF",
    desc = "Strategy: Always defect regardless of the opponent's move.\nDescription: Maximizes personal payoff but often leads to mutual defection and lower overall payoffs in repeated interactions.",
    strategy_type = "NASTY",
    logic = defector_logic
)


def tester_logic(prev_results,place):
    if len(prev_results) % 3 == 0:
        return 0

    if len(prev_results) > 3:
        check = prev_results[(len(prev_results)//2)*3][int(not place)]

        if check:
            return 0
        else:
            return 1


tester = Strategy(
    name = "Tester",
    st_id = "TES",
    desc = "Strategy: Defects to check how opponent reacts and tries taking advantage of them.\nDescription: Tests opponents based on reaction. And Defects on Every 3rd Turn",
    strategy_type = "NASTY",
    logic = tester_logic
)

strategies = [
    tit_for_tat,
    win_stay_lose_shift,
    pavlov,
    random_st,
    grim_trigger,
    tit_for_2_tat,
    soft_tit_for_tat,
    forgiving_tit_for_tat,
    reverse_tit_for_tat,
    cooperator,
    defector,
    tester
    ]