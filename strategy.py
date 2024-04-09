from typing import Callable, List

class Strategy:
    def __init__(self, name: str, st_id: str, desc: str, strategy_type: str, logic: Callable[[List[int]], int]) -> None:
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
    
    
    def giveNextChoice(self, prev_results: List[int]) -> int:
        """
        Calculates the next choice based on the previous results.
        
        Args:
            prev_results (List[int]): List of previous results.
            
        Returns:
            int: The next choice.
        """
        if not isinstance(prev_results, list):
            raise ValueError("prev_results must be a list")
        
        return self.logic(prev_results)