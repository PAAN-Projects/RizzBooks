import os
import sqlite3


class ORM:
    def __init__(self):
        self.db_location = './database.db'
        self.db_connection = sqlite3.connect(self.db_location)
        self.db_cursor = self.db_connection.cursor()
        empty = self.db_cursor.execute(
            "SELECT name FROM sqlite_schema").fetchall()
        if empty == []:
            self.__createDefaultTable()

    def __createDefaultTable(self):
        self.db_cursor.executescript("""
                                    CREATE TABLE Users (
                                    UserID int,
                                    UserName varchar(255),
                                    UserYear int,
                                    UserAge int
                                );
                                    CREATE TABLE Books (
                                    BookID int,
                                    BookName varchar(255),
                                    BookDescription varchar(255),
                                    BookYear int,
                                    BookRating int,
                                    BookImage BLOB,
                                    BookRatedAge int,
                                    BookStock int
                                );
                                """)
        self.db_connection.commit()

    def addBook(self, book_id, book_name, book_description, book_year, book_rating, book_image, book_ratedage, book_stock):
        self.db_cursor.execute("""
                                INSERT INTO Books(
                                    BookID,
                                    BookName,
                                    BookDescription,
                                    BookYear,
                                    BookRating,
                                    BookImage,
                                    BookRatedAge,
                                    BookStock
                                )
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                               """, (book_id, book_name, book_description, book_year, book_rating, book_image, book_ratedage, book_stock))
        self.db_connection.commit()

    def addUser(self, user_id, user_name, user_year, user_age):
        self.db_cursor.execute("""
                                INSERT INTO Books(
                                    UserID,
                                    UserName,
                                    UserYear,
                                    UserAge 
                                )
                                VALUES (?, ?, ?, ?);
                               """, (user_id, user_name, user_year, user_age))
        self.db_connection.commit()
