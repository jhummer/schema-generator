import factory
from api.models import Person, Task, Meeting, MeetingType, MeetingTaskPerson


class MeetingTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MeetingType

    name = "Veckomöte"
    period = "Monthly"
    occurences = 1

    @factory.post_generation
    def tasks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            print("doing nothin")
            return

        if extracted:
            # A list of tasks were passed in, use them
            for task in extracted:
                self.tasks.add(task)


class MeetingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Meeting

    meeting_type = factory.SubFactory(MeetingTypeFactory)
    date = factory.Faker("date_object")


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    name = factory.Faker("name")
    print(f"name: {name}")


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Faker("job")
    assignee_count = 1

    @factory.post_generation
    def qualifiers(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            print("doing nothin")
            return

        if extracted:
            # A list of qualifiers were passed in, use them
            for person in extracted:
                self.qualifiers.add(person)


class MTPFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MeetingTaskPerson

    meeting = factory.SubFactory(MeetingFactory)
    task = factory.SubFactory(TaskFactory)
    person = factory.SubFactory(PersonFactory)
