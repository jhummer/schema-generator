import pytest
from api.utils import assign_task


@pytest.mark.django_db
def test_assign_task(
    person_factory, task_factory, meeting_factory, meeting_type_factory, mtp_factory
):
    print("PERSONS:")
    persons1 = person_factory.create_batch(3)
    print(persons1)
    persons2 = person_factory.create_batch(3)
    print(persons2)
    print("TASKS:")
    task1 = task_factory.create(qualifiers=persons1)
    print(task1)
    task2 = task_factory.create(qualifiers=persons2)
    print(task2)
    print("MEETING TYPE:")
    meeting_type = meeting_type_factory.create(tasks=[task1, task2])
    print(meeting_type)
    print("MEETING:")
    meeting = meeting_factory.create(meeting_type=meeting_type)
    print(meeting)
    mtp1 = mtp_factory(meeting=meeting, task=task1, person=persons1[0])
    mtp2 = mtp_factory(meeting=meeting, task=task2, person=persons1[1])
    print("MTP")
    print(mtp1)
    print(mtp2)

    assignee = assign_task(task1, meeting)
    print(assignee)
    print(list(task1.qualifiers.all()))
    assert assignee == persons1[2]
