class Outcome:
    """This class dscribes a single outcome.
    
    An outcome is what the learner is expected to be able to accomplish after the task or project. An example 
    is 'Create a Repository on GitHub.'.
    """
    def __init__(self, text: str):
        self.__text = text