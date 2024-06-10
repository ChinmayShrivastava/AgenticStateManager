from asmanager.statemanager.StateManager import StateManager, State
from asmanager.environment.Environment import Environment
from asmanager.actions.Actions import Actions

class Task:
    def __init__(
        self,
        task: str,
        state: State = None,
        environment: Environment = None,
        actions: Actions = None
    ):
        self.task = task

        self.state_manager = StateManager(state) if state is not None \
            else StateManager()
        
        self.environment = environment if environment is not None \
            else Environment()
        
        self.actions = actions if actions is not None \
            else Actions()

    def __str__(self):
        return self.task