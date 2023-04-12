from dotenv import load_dotenv
import os
from code_scanner import CodeScanner

load_dotenv()
GITHUB_API_KEY = os.environ['GITHUB_API_KEY']
code_scanner = CodeScanner(GITHUB_API_KEY)
github_client = code_scanner.get_github_client()
user = code_scanner.create_user('lyle', 'lyle@gmail.com')
resource = code_scanner.create_project_resource(
    name='Python Random Module on W3.',
    description='An article on the Python Random module from W3.',
    resource_type='article',
    resource_url='https://www.w3schools.com/python/module_random.asp'
)

"""Create our first project"""

title = 'PROJECT ONE'

description = '''
This is a simple project that requires the student to create a simple repo, a project 
folder and then a python file with a single function that generates two random numbers.
'''

outcomes = [
    'Create a Repository on GitHub.',
    'Clone a Remote Repo to Your Local Development Environment.'
]

resources = [
    resource
]

instructions = [
    'Use Python3.10 for the tasks.',
    'Use Ubuntu 22.04 for the tasks.',
    'You must have a github account.'
]

project_repo = 'SimpleScan'

project_folder = 'test_folder'

project_one = code_scanner.create_project(
    project_title=title,
    project_description=description,
    project_outcomes=outcomes,
    project_resources=resources,
    project_instructions=instructions,
    project_repo=project_repo,
    project_folder=project_folder
)

if __name__ == '__main__':
    print(project_one)