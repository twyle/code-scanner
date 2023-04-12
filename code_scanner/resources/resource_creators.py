from .utils.task_output import TaskOutput
from .resource import Resource
from .utils.instruction import Instruction
from .task import Task
from .project import Project
from .utils.project_outcome import ProjectOutcome


def create_task_output(output_files: list[str], project=None):
    task_one_outputs = TaskOutput()
    task_one_outputs.create_output_files(output_files, project)
    return task_one_outputs 


def create_task(
    project_id: int,
    task_title: str,
    task_description: str,
    task_resources: list[Resource],
    task_instructions: list[Instruction]
) -> Task:
    task = Task(
        project_id,
        task_title,
        task_description,
        task_resources,
        task_instructions
    )
    
    return task

def save_task(task: Task):
    """Save a task to database."""
    pass


def create_project_(
    project_title: str,
    project_description: str,
    project_outcomes: list[ProjectOutcome],
    project_resources: list[Resource],
    project_instructions: list[Instruction],
    project_repo: str,
    project_folder: str
) -> Project:
    project = Project(
        project_title,
        project_description,
        project_outcomes,
        project_resources,
        project_instructions,
        project_repo,
        project_folder
    )
    
    return project

def save_project(project: Project):
    """Save project to database."""
    pass