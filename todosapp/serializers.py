from rest_framework import serializers

from todosapp.models import Project, TodoItem


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    repo_link = serializers.URLField()
    contributors = serializers.StringRelatedField(many=True)
    created_at = serializers.DateTimeField()

    class Meta:
        model = Project
        fields = ['name', 'repo_link', 'contributors', 'created_at']


class ToDoItemModelSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = TodoItem
        fields = ['project', 'text', 'owner', 'created_at', 'updated_at',
                  'is_active']
