from typing import Callable, List

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
            prev_results (List[int]): List of previous results.

        Returns:
            int: The next choice.
            (1 - Cooperate, 0 - Defect)
        """
        if not isinstance(prev_results, list):
            raise ValueError("prev_results must be a list")

        return self.logic(prev_results, place)


def tit_for_tat_logic(prev_results,place):
    """
    Prev_Results : [[1/0,1/0]] - [0th Strategy, 1st Strategy]
    (1 - Cooperate, 0 - Defect)
    """
    if len(prev_results) == 0:
        return 1
    
    last_result = prev_results[-1]

    return last_result[1] if place == 0 else last_result[0]


tit_for_tat = Strategy(
    name = "Tit For Tat", st_id = "TFT",
    desc = "Forgiving but firm, as it retaliates against defection but forgives and returns to cooperation if the opponent cooperates again.",
    strategy_type = "NICE",
    logic = tit_for_tat_logic
)

print(tit_for_tat.name)
print(tit_for_tat.st_id)
print(tit_for_tat.desc)
print(tit_for_tat.strategy_type)