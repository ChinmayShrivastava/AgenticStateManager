import asyncio̦

from asmanager.actions.Actions import Actions
from asmanager.environment.Environment import Environment
from asmanager.statemanager.StateManager import State, StateManager


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
        
        ###
        self._initialized = False

    def __str__(self):
        return self.task
    
    def generate_steps(self):
        self._generate_steps()
        self._initialized = True
        pass

    async def agenerate_steps(self):
        await self._agenerate_steps()
        self._initialized = True
        pass

    # code to complete steps iteratively