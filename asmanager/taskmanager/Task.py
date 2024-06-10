class Task:
    def __init__(
        self,
        task: str,
    ):
        self.task = task

    def __str__(self):
        return self.task