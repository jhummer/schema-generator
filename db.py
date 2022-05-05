import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("assignments.db")

    def create_db(self):
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS assignments
            ([id] INTEGER PRIMARY KEY, [name] TEXT, [assignment] TEXT, [date] TEXT)
            """
        )
        self.conn.commit()

    def get_latest(self, assignment):
        q = """select name, assignment, date from assignments group by name order by date(date) desc;"""
        cur = self.conn.cursor()
        cur.execute(q)
        rows = cur.fetchall()
        return rows

    def save(self, name, assignment, date):
        q = f"""insert into assignments (name, assignment, date) values('{name}', '{assignment}', '{date}');"""
        cur = self.conn.cursor()
        cur.execute(q)
        self.conn.commit()
