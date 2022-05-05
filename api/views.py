from rest_framework import viewsets

from api.models import Meeting, Task, Person, MeetingTaskPerson
from api.serializers import (
    MeetingSerializer,
    TaskSerializer,
    PersonSerializer,
    MeetingTaskPersonSerializer,
)


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class MeetingTaskPersonViewSet(viewsets.ModelViewSet):
    queryset = MeetingTaskPerson.objects.all()
    serializer_class = MeetingTaskPersonSerializer
