import pytest
from api.utils import assign_task


@pytest.mark.django_db
def test_assign_task_to_available_person(
    person_factory, task_factory, meeting_factory, meeting_type_factory, mtp_factory
):
    """Test assigning a task to meeting with three persons qualified for three tasks
    where two of the persons are already assigned to another task at the same event."""

    persons1 = person_factory.create_batch(3)
    task1 = task_factory.create(qualifiers=persons1)
    task2 = task_factory.create(qualifiers=persons1)
    task3 = task_factory.create(qualifiers=persons1)
    meeting_type = meeting_type_factory.create(tasks=[task1, task2, task3])
    meeting = meeting_factory.create(meeting_type=meeting_type)
    mtp1 = mtp_factory(meeting=meeting, task=task1, person=persons1[0])
    mtp2 = mtp_factory(meeting=meeting, task=task2, person=persons1[1])

    assignee = assign_task(task3, meeting)
    assert assignee == persons1[2]
