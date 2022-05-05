import calendar
from django.db import models


class Meeting(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    meeting_type = models.ForeignKey("MeetingType", on_delete=models.CASCADE)

    @property
    def weekday(self):
        return calendar.day_name[self.date.weekday()]

    @property
    def month(self):
        return calendar.month_name[self.date.month()]

    def __str__(self):
        return f"{self.name} {self.weekday} {self.date}"


class MeetingType(models.Model):
    DAILY = "D"
    WEEKLY = "W"
    MONTHLY = "M"
    YEARLY = "Y"

    PERIOD_CHOICES = [
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
        (MONTHLY, "Monthly"),
        (YEARLY, "Yearly"),
    ]

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    tasks = models.ManyToManyField("Task")
    period = models.CharField(max_length=32, choices=PERIOD_CHOICES)
    occurences = models.IntegerField()  # occurences per period

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    assignee_count = models.IntegerField()
    qualifiers = models.ManyToManyField(
        Person, related_name="qualified_for", blank=True
    )
    # can only have this task at event
    singleton = models.BooleanField(default=True)
    # this task blacklists these other tasks
    blacklists = models.ManyToManyField(
        "self", symmetrical=False, related_name="blacklisted_by"
    )
    # rank          - ranking of the task?
    # standin       - possible
    # whitelists    - these other tasks can be had while having this task

    def __str__(self):
        return self.name


class MeetingTaskPerson(models.Model):
    meeting = models.ForeignKey(
        Meeting, related_name="assignees", on_delete=models.CASCADE
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.meeting.date} {self.task}: {self.person.name}"


# Schema related or meeting?


class Period(models.Model):
    # Montly, Weekly, Yearly
    period_type = models.CharField(max_length=7)
