from django.db import models
from django.utils.translation import gettext_lazy as _



class Project(models.Model):
    TYPE_CHOICES = [
        ('backend', _('Backend')),
        ('frontend', _('Frontend')),
        ('ios', _('iOS')),
        ('android', _('Android')),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

class Issue(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', _('Low')),
        ('MEDIUM', _('Medium')),
        ('HIGH', _('High')),
    ]

    TAG_CHOICES = [
        ('BUG', _('Bug')),
        ('FEATURE', _('Feature')),
        ('TASK', _('Task')),
    ]

    STATUS_CHOICES = [
        ('TODO', _('To Do')),
        ('INPROGRESS', _('In Progress')),
        ('FINISHED', _('Finished')),
    ]

    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    assigned_to = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='TODO')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Comment(models.Model):
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE)
    author = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.email} on {self.issue.name}'


class Contributor(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} - {self.project.name}'