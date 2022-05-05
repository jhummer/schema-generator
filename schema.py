import random
from calendar import monthrange
from datetime import datetime

from dateutil.rrule import rrule, WEEKLY, TU, SU
from dateutil.parser import parse

import click
import yaml


class Assignment:
    def __init__(self, name, assignee_count, candidates):
        self.name = name
        self.assignee_count = assignee_count
        self.candidates = candidates

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"

    def sorted_candidates(self):
        pass

    def generate_assignees(self):
        # TODO:
        # Get previous assignees from db
        # Check latest date assigned.
        # Check not already assigned to another assignment
        assigned = random.choice(self.candidates)
        print(self, assigned)


class AssignmentDay:
    def __init__(self, date):
        self.date

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.date}>"


@click.command()
@click.option("--date", help="Month of schedule")
def main(date):
    dtstart = datetime.strptime(date, "%Y%m")
    dtend = datetime.strptime(
        date + str(monthrange(dtstart.year, dtstart.month)[1]), "%Y%m%d"
    )
    print(f"Start: {dtstart}")
    print(f"End: {dtend}")
    days = list(
        rrule(
            WEEKLY,
            byweekday=(TU, SU),
            dtstart=parse(str(dtstart)),
            until=parse(str(dtend)),
        )
    )
    print(days)

    with open("assignments.yml", "r") as f:
        yml_assignments = yaml.safe_load(f)

    assignments = []
    for a in yml_assignments:
        assignment = Assignment(**a)
        assignment.generate_assignees()


if __name__ == "__main__":
    main()
