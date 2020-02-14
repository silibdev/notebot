from datetime import datetime
from enum import Enum


class Priority(Enum):
    HIGH = 'High'
    MEDIUM = 'Medium'

    def __str__(self):
        return self.value


class TaskModel:

    def __init__(self, title, description='', priority: Priority = None, due_date: datetime = None):
        self.id = ''
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.isDone = False

    def __str__(self):
        task = '{}\n'.format(self.id)

        if self.priority:
            task += ':{}:'.format(self.priority)

        task += '{}'.format(self.title)

        if self.description:
            task += '\n{}'.format(self.description)

        if self.due_date:
            task += '\n{}'.format(self.due_date.strftime('%d-%b-%y %H:%M'))

        if self.isDone:
            task += '\nDONE'

        return task
