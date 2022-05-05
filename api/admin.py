from django.contrib import admin
from .models import Meeting, Task, Person, MeetingTaskPerson, MeetingType

admin.site.register(Meeting)
admin.site.register(Task)
admin.site.register(Person)
admin.site.register(MeetingTaskPerson)
admin.site.register(MeetingType)
