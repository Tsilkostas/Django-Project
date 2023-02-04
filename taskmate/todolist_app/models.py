from django.db import models

""" Creation of database models """
class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    """ Method to make Task list object(from admin panel) a string """
    def __str__(self):
        return self.task + " - " + str(self.done)
