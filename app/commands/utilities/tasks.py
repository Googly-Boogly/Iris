from app.commands.utilities.classes_utilities import tasks
from datetime import datetime


def create_task(task_name: str, due_date: datetime, description: str = 'None',
                priority: str = 'Medium', status: str = 'To_Do') -> bool:
    """
    creates a task in the database
    :param task_name: (str) the title or name of the task
    :param description: (str) a more detailed description of the task
    :param due_date: (datetime) iso format of when this task needs to be done
    :param priority: (str) Either low medium or high
    :param status: (str) either: To_Do, In_progress, or completed
    :return: sql out
    """
    data = {
        'task_name': task_name,
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'added': datetime.now(),
        'updated': datetime.now(),
        'status': status
    }
    return tasks.save(data)


def get_tasks() -> list:
    tot_tasks = tasks.select_all()
    return tot_tasks


if __name__ == '__main__':
    # print(create_alarm_with_repeat(repeat_days='Monday Tuesday Wednesday Friday', time='07:30'))
    print(create_task(task_name='Do the dishes', description='finish cleaning the dishes', due_date='2023-10-14', priority='high', status='to_do'))