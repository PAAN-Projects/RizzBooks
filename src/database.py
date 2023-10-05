import os
import sqlite3


class ORM:
    def __init__(self):
        self.db_location = './database.db'
        self.db_connection = sqlite3.connect(
            self.db_location, check_same_thread=False)
        self.db_cursor = self.db_connection.cursor()
        empty = self.db_cursor.execute(
            "SELECT name FROM sqlite_schema").fetchall()
        if empty == []:
            self.__createDefaultTable()

    def __createDefaultTable(self):
        """
            Private function: this function can't be accessed outside of this class

            @summary: This Function creates basic database struct if database is not found
        """
        self.db_cursor.executescript("""
                                    CREATE TABLE Users (
                                    UserID int,
                                    UserName varchar(255),
                                    UserYear int,
                                    UserAge int,
                                    UserPass varchar(255),
                                    PRIMARY KEY (UserID),
                                    UNIQUE(UserName)
                                );
                                    CREATE TABLE Books (
                                    BookID int,
                                    BookName varchar(255),
                                    BookDescription varchar(255),
                                    BookYear int,
                                    BookRating int,
                                    BookRatedAge int,
                                    BookStock int,
                                    BookGenre varchar(255),
                                    BookSellerID int,
                                    PRIMARY KEY (BookID),
                                    FOREIGN KEY (BookSelLerID) REFERENCES Users(UserID)
                                );
                                """)
        self.db_connection.commit()

    def addBook(self, user_name, book_id, book_name, book_description, book_year, book_rating, book_ratedage, book_stock, book_genre):
        self.db_cursor.execute("""
                                    SELECT * FROM Users
                                    WHERE UserName=?
                               """, (user_name,))
        user = self.db_cursor.fetchall()
        print(user)
        self.db_cursor.execute("""
                                INSERT INTO Books(
                                    BookID,
                                    BookName,
                                    BookDescription,
                                    BookYear,
                                    BookRating,
                                    BookRatedAge,
                                    BookStock,
                                    BookGenre,
                                    BookSellerId
                                )
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                               """, (book_id, book_name, book_description, book_year, book_rating, book_ratedage, book_stock, book_genre, user[0][0]))
        self.db_connection.commit()

    def addUser(self, user_id, user_name, user_year, user_age, user_pass):
        self.db_cursor.execute("""
                                INSERT INTO Users(
                                    UserID,
                                    UserName,
                                    UserYear,
                                    UserAge,
                                    UserPass
                                )
                                VALUES (?, ?, ?, ?, ?);
                               """, (user_id, user_name, user_year, user_age, user_pass))
        self.db_connection.commit()

    def getUser(self, user_name):
        self.db_cursor.execute("""
                                SELECT * FROM Users
                                WHERE UserName=?
                               """, (user_name,))
        user = self.db_cursor.fetchall()
        return user[0]

    def getAllBooks(self):
        self.db_cursor.execute("""
                               SELECT * FROM Books
                               """)
        books = self.db_cursor.fetchall()
        return books

    def delAllUsers(self):
        self.db_cursor.execute("""
                               DELETE FROM Users
                               """)
        self.db_connection.commit()

    def delAllBooks(self):
        self.db_cursor.execute("""
                               DELETE FROM Books
                               """)
        self.db_connection.commit()
