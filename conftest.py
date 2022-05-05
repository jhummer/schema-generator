import pytest
from pytest_factoryboy import register
from tests.factories import (
    TaskFactory,
    PersonFactory,
    MeetingTypeFactory,
    MeetingFactory,
    MTPFactory,
)

register(TaskFactory)  # fixture name: user_factory
register(PersonFactory)
register(MeetingFactory)
register(MeetingTypeFactory)
register(MTPFactory)


@pytest.fixture(scope="session")
def meeting(db, task, meeting_factory, meeting_type_factory):
    meeting_type = meeting_type_factory.create(tasks=[task])
    meeting = meeting_factory.create(meeting_type=meeting_type)
    return meeting


@pytest.fixture
def person(db, person_factory):
    person = person_factory.create()
    return person


@pytest.fixture
def task(db, task_factory, person_factory):
    persons = person_factory.create_batch(2)
    task = task_factory.create(qualifiers=persons)
    return task
