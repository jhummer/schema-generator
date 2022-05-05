from rest_framework import serializers
from api.models import Meeting, Task, Person, MeetingTaskPerson


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["name", "description", "assignee_count", "qualifiers"]


class TaskPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "description"]


class PersonSerializer(serializers.ModelSerializer):
    qualified_for = TaskPersonSerializer(many=True, required=False)

    class Meta:
        model = Person
        fields = ["name", "qualified_for"]


class MeetingTaskPersonSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    task = TaskSerializer()

    class Meta:
        model = MeetingTaskPerson
        fields = ("id", "meeting", "task", "person")


class MeetingSerializer(serializers.ModelSerializer):
    assignees = MeetingTaskPersonSerializer(many=True, required=False)

    class Meta:
        model = Meeting
        fields = [
            "id",
            "name",
            "description",
            "date",
            "meeting_type",
            "assignees",
        ]
