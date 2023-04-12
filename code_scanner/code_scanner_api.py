from .oauth import OAuth
from .resources.user import User
from .resources.resource import Resource
from .resources.utils.resource_type import ResourceType
from .resources import create_project_
from .resources.utils.project_outcome import ProjectOutcome
from .resources.utils.instruction import Instruction

class CodeScanner:
    def __init__(self, github_api_key):
        self.__github_client = self.__authenticate_github(github_api_key)
        
    
    def __authenticate_github(self, github_api_key):
        oauth = OAuth(github_api_key)
        github_client = oauth.authenticate()
        return github_client
    
    def get_github_client(self):
        return self.__github_client
    
    def create_user(self, user_name, email):
        user = User(user_name, email)
        return user
    
    def create_project_resource(self, name, description, resource_type, resource_url):
        if resource_type == 'youtube video':
            resource_type = ResourceType.YOUTUBE_VIDEO
        elif resource_type == 'article':
            resource_type = ResourceType.ARTICLE
            
        resource = Resource(
            name=name,
            description=description,
            resource_type=resource_type,
            resource_url=resource_url
        )
        return resource
    
    def create_project(
        self,
        project_title: str,
        project_description: str,
        project_outcomes: list[str],
        project_resources: list[Resource],
        project_instructions: list[str],
        project_repo: str,
        project_folder: str
    ):
        outcomes = [ProjectOutcome(text) for text in project_outcomes]
        instructions = [Instruction(text) for text in project_instructions]
        project = create_project_(
            project_title=project_title,
            project_description=project_description,
            project_outcomes=outcomes,
            project_resources=project_resources,
            project_instructions=instructions,
            project_repo=project_repo,
            project_folder=project_folder
        )
        
        return project
        