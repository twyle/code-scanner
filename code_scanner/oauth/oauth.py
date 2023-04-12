from github import Github

class OAuth:
    def __init__(self, github_api_key):
        self.__github_api_key = github_api_key
        self.__github_client = None
        
    def authenticate(self):
        if not self.__github_client:
            self.__github_client = Github(self.__github_api_key)
        return self.__github_client