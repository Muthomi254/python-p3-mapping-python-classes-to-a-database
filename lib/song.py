from config import CONN, CURSOR

import pytest; 
import sqlite3

# Establishing a connection to the database
CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

# Defining the class their values
class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()  # To commit changes to the database

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()  # To commit changes to the database

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
