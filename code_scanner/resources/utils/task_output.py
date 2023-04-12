from .output import OutPut


class TaskOutput(OutPut):
    def __init__(self):
        self.__output_repo = None
        self.__project_folder = None
        self.__output_files = None
        
    def __get_project_repo(self, project):
        self.__output_repo = project.get_project_repo()
    
    def __get_project_folder(self, project):
        self.__project_folder = project.get_project_folder()
        
    def create_output_files(self, output_files: list[str], project=None):
        if project:
            self.__get_project_repo(project)
            self.__get_project_folder(project)
            self.__output_files = [os.path.join(self.__output_repo, self.__project_folder, output_file)
                                  for output_file in output_files]
        else:
            self.__output_files = output_files
        
    def get_output_files(self):
        return self.__output_files
