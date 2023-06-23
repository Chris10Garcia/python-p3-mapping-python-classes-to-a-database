from config import CONN, CURSOR
import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Song:

    all = []

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
        self.add_to_all_songs(self)

    @classmethod
    def add_to_all_songs(cls, song):
        cls.all.append(song)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            );
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]


    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

# hello = Song("Hello", 25)
# hello.save()

# despacito = Song ("Despacito", "Vida")
# despacito.save()

# songs = CURSOR.execute('SELECT * FROM songs')

# for row in songs:
#     print(row)