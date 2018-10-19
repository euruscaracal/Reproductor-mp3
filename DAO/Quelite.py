import sqlite3

class Quelite():

    def __init__(self):

            self.bd = sqlite3.connect("rolas.db")
            self.cursor = self.bd.cursor()
            self.types()
            self.performers()
            self.persons()
            self.groups()
            self.albums()
            self.rolas()
            self.in_group()

    def insert(self):
        person = [
            """
            INSERT INTO types VALUES(0,'Person');
            """
            ]
        for p in person:
            self.bs.execute(p)
        group = [
            """
            INSERT INTO types VALUES(1,'Group');
            """
            ]
        for g in group:
            self.bs.execute(g)
        unknown = [
            """
            INSERT INTO types VALUES(2,'Unknown');
            """
            ]
        for unk in unknown:
            self.bs.execute(unk)

    def performers(self):
        performers = [
            """
            CREATE TABLE IF NOT EXISTS performers(
                id_performer    INTEGER PRIMARY KEY,
                id_type         INTEGER,
                name            TEXT,
                FOREIGN KEY     (id_type) REFERENCES types(id_type)
            );
            """
        ]
        for performer in performers:
            self.bs.execute(performer)

    def persons(self):
        persons = [
            """
            CREATE TABLE IF NOT EXISTS persons(
                id_person   INTEGER PRIMARY KEY,
                stage_name  TEXT,
                real_name   TEXT,
                birth_date  TEXT,
                end_date    TEXT
            );
            """
        ]
        for person in persons:
            self.bs.execute(person)

    def groups(self):
        groups = [
            """
            CREATE TABLE IF NOT EXISTS groups(
                id_group    INTEGER PRIMARY KEY,
                name        TEXT,
                start_date  TEXT,
                end_date    TEXT
            );
            """
        ]
        for group in groups:
            self.bs.execute(group)

    def albums(self):
        albums = [
            """
            CREATE TABLE IF NOT EXISTS albums(
                id_album    INTEGER PRIMARY KEY,
                path        TEXT,
                name        TEXT,
                year        INTEGER
            );
            """
        ]
        for album in albums:
            self.bs.execute(album)

    def rolas(self):
        tracks = [
            """
            CREATE TABLE IF NOT EXISTS tracks(
                id_track        INTEGER PRIMARY KEY,
                id_performer    INTEGER,
                id_album        INTEGER,
                path            TEXT,
                title           TEXT,
                track           INTEGER,
                year            INTEGER,
                genre           TEXT,
                FOREIGN KEY     (id_performer) REFERENCES performers(id_performer),
                FOREIGN KEY     (id_album) REFERENCES albums(id_album)
            );
            """
        ]
        for track in tracks:
            self.bs.execute(track)

    def create_table_in_groups(self):
        in_groups = [
            """
            CREATE TABLE IF NOT EXISTS in_group(
                id_person   INTEGER,
                id_group    INTEGER,
                PRIMARY KEY (id_person, id_group),
                FOREIGN KEY (id_person) REFERENCES persons(id_person),
                FOREIGN KEY (id_group) REFERENCES groups(id_group)
            );
            """
        ]
        for in_group in in_groups:
            self.bs.execute(in_group)



database = DataBase()
