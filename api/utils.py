import random
from api.models import Meeting, Task, Person, MeetingTaskPerson


def assign_task(task: Task, meeting: Meeting) -> Person:
    """Return the person who is next in line for the given task.
    Either a new person qualified for the task or the one who had
    the task the longest time ago.
    """
    print(f"QUALIFIERS for {task}: {task.qualifiers.all()}")
    # print(f"ASSIGNEES AT MEETING: {meeting.assignees.all()}")
    latest_assigned_task = MeetingTaskPerson.objects.filter(task=task).order_by(
        "meeting__date"
    )
    if not latest_assigned_task:
        print(f"No one has been assigned {task} before. Pick one who's available.")
        for person in task.qualifiers.all():
            if is_available(person, meeting):
                return person
        else:
            print("No one is available")

    print(f"pick the one who had {task} the longest ago or never")
    print(latest_assigned_task)
    never_assigned = []
    for qualifier in task.qualifiers.all():
        # for every qualifier
        assigned = False
        print(f"[+] CHECK ASSIGNMENTS for {qualifier}")
        for mtp in latest_assigned_task:
            if mtp.task == task:
                if mtp.person == qualifier:
                    print(f"{qualifier} was assigned {task} @ {mtp.meeting}")
                    assigned = True
                    # has been assigned,
                if not assigned:
                    print(f"{qualifier} has never been assigned {task}")
                    never_assigned.append(qualifier)

    for person in never_assigned:
        print(f"{person} has never been assigned {task}. Is {person} available?")
        # check if already assigned another task
        if is_available(person, meeting):
            print(f"{person} is available")
            return person
        else:
            # can this task be handled together with the other task?
            # TODO: check rank/blacklist etc
            continue

    return assignee


def is_available(person: Person, meeting: Meeting) -> bool:
    """Check if person is assigned to another task at the same meeting"""
    persons_assigned = [mtp.person for mtp in meeting.assignees.all()]
    if person in persons_assigned:
        print(f"{person} IS assigned @ {meeting}")
        return False
    print(f"{person} is NOT assigned to other task @ {meeting}")
    return True
