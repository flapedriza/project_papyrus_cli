import datetime as dt

class Task:

    def __init__(self,name,priority,user,deadline,description,project,tags):
        self.name = name
        self.priority = priority
        self.user = user
        self.deadline = deadline
        self.description = description
        self.project = project
        self.tags = tags
        self.completed = False

    def toServer(self):
        return self.__dict__

    @staticmethod
    def fromServer(record):
        task = Task(record['title'],record['priority'],record['expiration_date'],
         record['description'],record['project'],record['tags'])
        task.completed = record['completed']
        return task
