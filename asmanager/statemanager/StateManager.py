from typing import Dict, List
from pydantic import BaseModel

from asmanager.utils.formatters import iterative_formatter

DEFAULT_STATE = {}

# eg state = {
#     "id1": {
#        "step_task": "some_task",
#        "dependencies": [],
#        "finished": False,
#        "required_info": {}
#     },
#     "id2": {
#        "step_task": "some_task",
#        "dependencies": ["some_key]
#        "finished": False,
#        "required_info": {}
#     }
# }

# BIG IDEA: Each state has steps. Each step can have more steps that then become dependent on the parent step.

class Step(BaseModel):
    step_task: str
    dependencies: list
    finished: bool
    required_info: dict

class State(BaseModel):
    state: Dict[str, Step]

    def __dict__(self):
        return self.state

def dependency_resolver(state: State):
    # this function returns the id of the next step to be executed
    # it should be a step that has no dependencies or all of its dependencies have been executed and finished
    id = None
    for k, v in state.items():
        if not v["finished"]:
            if len(v["dependencies"]) == 0:
                id = k
                break
            else:
                all_deps_finished = True
                for dep in v["dependencies"]:
                    if not state[dep]["finished"]:
                        all_deps_finished = False
                        break
                if all_deps_finished:
                    id = k
                    break
    return id

class StateManager:
    def __init__(
        self,
        state: State = None,
    ):
        self.state = state if state is not None \
            else State(state=DEFAULT_STATE)
        
        self._current_step_id = dependency_resolver(self.state)

    def _tostring(self):
        return iterative_formatter(self.state)
    
    def __str__(self):
        return self._tostring()
    
    def set_state(self, state):
        self.state = state
        self._current_step_id = dependency_resolver(self.state)

    def get_state(self):
        return self.state

    def get_current_step(self):
        return self.state[self._current_step_id]

    def finish_current_step(self):
        self.state[self._current_step_id]["finished"] = True
        self._current_step_id = dependency_resolver(self.state)

    def get_current_step_id(self):
        return self._current_step_id
    
    def is_complete(self):
        return self._current_step_id is None
    
    def add_step(self, step: Step):
        self.state[len(self.state)] = step