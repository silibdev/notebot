from typing import List


class TaskModel:
    FORMAT = 'Id-Name-Description-Tags-Done'

    def __init__(self, title, description='', tags=None):
        self.id = ''
        self.title = title
        self.description = description
        self.tags = tags or []
        self.isDone = False

    def __str__(self):
        return '{}-{}-{}-{}-{}'.format(self.id, self.title, self.description, self.tags, self.isDone)
