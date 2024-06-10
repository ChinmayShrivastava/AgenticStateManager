class Actions:
    def __init__(
        self
    ):
        self.actions = []

    def __str__(self):
        return self._tostring()
    
    def get_actions(self):
        return self.actions