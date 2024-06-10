from typing import Dict

from asmanager.utils.formatters import iterative_formatter

QUESTIONS_KEY = "ai_questions"

class StateManager:
    def __init__(
        self,
        state: Dict,
    ):
        self.state = state

    def _tostring(self):
        return iterative_formatter(self.state)
    
    def __str__(self):
        return self._tostring()
    
    def get_state(self):
        return self.state
    
    def update_state(self, new_state):
        self.state = new_state