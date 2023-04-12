from ..utils.instruction import Instruction
from ..resource import Resource
from ..utils.task_output import TaskOutput


class Task:
    def __init__(
        self,
        project_id: int,
        task_title: str,
        task_description: str,
        task_resources: list[Resource],
        task_instructions: list[Instruction],
        main_file_lines: str = ''
    ):
        self.__project_id = project_id
        self.__task_title = task_title
        self.__task_description = task_description
        self.__task_resources = task_resources
        self.__task_instructions = task_instructions
        self.__task_outputs = None
        self.__main_file_lines = main_file_lines
        
    def get_main_file_lines(self):
        return self.__main_file_lines
    
    def get_task_id(self):
        #TODO
        return 1
        
    def get_instructions(self):
        return self.__project_instructions

    def add_instruction(self, instruction: Instruction):
        pass
    
    def delete_instruction(self, instruction: Instruction):
        pass

    def create_outputs(self, outputs: TaskOutput):
        self.__task_outputs = outputs
    
    def add_output(self):
        pass
    
    def delete_output(self):
        pass
    
    def get_outputs(self):
        return self.__task_outputs.get_output_files()
    
    def create_resource(self):
        pass
    
    def add_resource(self):
        pass
    
    def delete_resource(self):
        pass

    def get_resources(self):
        pass
    
    def create_checks(self, checks):
        pass
    
    def get_checks(self):
        pass