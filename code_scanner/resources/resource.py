from .utils.resource_type import ResourceType

class Resource:
    def __init__(self, name: str, description: str, resource_type: ResourceType, 
                resource_url: str):
        self.__resource_name = name
        self.__resource_description = description
        self.__resource_type = resource_type
        self.__resource_url = resource_url   