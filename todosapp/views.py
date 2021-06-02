from djangorestframework_camel_case.render import CamelCaseJSONRenderer, \
    CamelCaseBrowsableAPIRenderer

from rest_framework.viewsets import ModelViewSet

from todosapp.models import Project, TodoItem
from todosapp.serializers import ProjectModelSerializer, \
    ToDoItemModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    renderer_classes = (CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer,)


class ToDoItemModelViewSet(ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = ToDoItemModelSerializer
    renderer_classes = (CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer,)
