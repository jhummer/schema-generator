import random
from api.models import Meeting, Task, Person, MeetingTaskPerson


def assign_task(task: Task, meeting: Meeting) -> Person:
    """Return the person who is next in line for the given task.
    Either a new person qualified for the task or the one who had
    the task the longest time ago.
    """
    # qualifiers = Person.objects.filter(qualified_for__in=[task])
    print(f"QUALIFIERS: {task.qualifiers.all()}")
    print(f"ASSIGNEES: {meeting.assignees.all()}")
    latest_assigned = MeetingTaskPerson.objects.filter(task=task).order_by(
        "meeting__date"
    )
    if not latest_assigned:
        print("Picking random assignee:")
        assignee = random.choice(task.qualifiers.all())
        return assignee

    print("pick the one who had the task the longest ago or never")
    never_assigned = []
    for qualifier in task.qualifiers.all():
        # for every qualifier
        assigned = False
        for mtp in latest_assigned:
            if mtp.person == qualifier:
                print(f"{qualifier} was assigned {mtp.meeting}")
                assigned = True
                # has been assigned,
        if not assigned:
            print(f"{qualifier} has never been assigned")
            never_assigned.append(qualifier)

    for person in never_assigned:
        rank = 0
        print(f"{person} has never been assigned {task}. Is {person} available?")
        # check if already assigned another task
        if person in meeting.assignees.all():
            # already assigned a task
            # is the assigned task conflicting with the new task?
            # TODO: handle conflicts/ranking/blacklist etc.
            print(f"{person} is not available")
            continue
        print(f"{person} is available")
        return person

    return assignee


def is_available(person: Person, meeting: Meeting) -> bool:
    """Check if person is assigned to another task at the same meeting"""
    for p in meeting.assignees.all():
        if p == person:
            print(f"{p} is assigned to: {p.task}")
            return False
    print(f"{person} is not assigned to any other task @ {meeting}")
    return True
