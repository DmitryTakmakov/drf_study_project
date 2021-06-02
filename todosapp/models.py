from uuid import uuid4

from django.db import models

from usersapp.models import User


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4,
                            verbose_name='uuid')
    name = models.CharField(max_length=64, unique=True,
                            verbose_name='project name')
    repo_link = models.URLField(null=True, verbose_name='link to project')
    contributors = models.ManyToManyField(User, related_name='project',
                                          verbose_name='project contributors')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='project created')

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4,
                            verbose_name='uuid')
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='todoitem',
                                verbose_name="item's project")
    text = models.TextField(max_length=500, verbose_name='item text')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='item created')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='item updated')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='users_todo', verbose_name='owner')
    is_active = models.BooleanField(default=False, verbose_name='active')
