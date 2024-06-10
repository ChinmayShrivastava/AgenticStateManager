class Environment:
    """
    Environment class
        Environment is the input provider. It notes all the inputs 
        available to the agent, and provides this input in a formatted 
        way when asked for it.
    """
    def __init__(
        self
    ):
        self.environment = {}

    def __str__(self):
        return self._tostring()
    
    def add_enviroment_by_step_id(self, step_id: str, environment: dict):
        # for each step, the environment is a dictionary of key-value pairs
        self.environment[step_id] = environment

    def get_environment_by_step_id(self, step_id: str):
        return self.environment[step_id]