from ..utils.project_outcome import ProjectOutcome
from ..utils.instruction import Instruction
from ..resource import Resource


class Project:
    def __init__(
        self,
        project_title: str,
        project_description: str,
        project_outcomes: list[ProjectOutcome],
        project_resources: list[Resource],
        project_instructions: list[Instruction],
        project_repo: str,
        project_folder: str,
        project_repo_type: str = 'public',
        project_repo_license: str = 'MIT',
        project_file_encoding: str = 'utf-8'
    ):
        self.__project_title = project_title
        self.__project_description = project_description
        self.__project_outcomes = project_outcomes
        self.__project_resources = project_resources
        self.__project_instructions = project_instructions
        self.__project_repo = project_repo
        self.__project_folder = project_folder
        self.__project_tasks = None
        self.__project_repo_type = project_repo_type
        self.__project_repo_license = project_repo_license
        self.__project_file_encoding = project_file_encoding
        
    def get_project_folder(self):
        return self.__project_folder
    
    def get_project_repo(self):
        return self.__project_repo
    
    def get_project_repo_type(self):
        return self.__project_repo_type
    
    def get_project_repo_license(self):
        return self.__project_repo_license
    
    def get_project_file_encoding(self):
        return self.__project_file_encoding
        
    def get_instructions(self):
        return self.__project_instructions

    def add_instruction(self, instruction: Instruction):
        pass
    
    def delete_instruction(self, instruction: Instruction):
        pass

    def create_outputs(self):
        pass
    
    def add_output(self):
        pass
    
    def delete_output(self):
        pass
    
    def get_outputs(self):
        pass
    
    def create_resource(self):
        pass
    
    def add_resource(self):
        pass
    
    def delete_resource(self):
        pass

    def get_resources(self):
        pass
    
    def get_outcomes(self):
        return self.__project_outcomes

    def add_outcome(self, outcome: ProjectOutcome):
        pass
    
    def delete_outcome(self, outcome: ProjectOutcome):
        pass