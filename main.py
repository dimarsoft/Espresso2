import sqlite3
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QTableWidget, QWidget, QPushButton, \
    QLabel, QLineEdit, QDialog, QComboBox, QDateTimeEdit

"""
Класс для работы с Базой данных.
1. подключение
2. выполнение запросов 
"""


class EspressoDb:
    def __init__(self, path_to_db):
        self.path_to_db = path_to_db

        self.db_connection = sqlite3.connect(path_to_db)
        self.cursor = self.db_connection.cursor()

    # Вывод БД в консоль
    def print(self):
        print("start print rows")
        rows = 0

        for row in self.cursor.execute("SELECT * FROM all_about_coffee"):
            print(row)
            rows += 1

        print(f"end print count rows = {rows}")


def test_db(path_to_db):
    try:
        database = EspressoDb(path_to_db)
        database.print()
    except sqlite3.DatabaseError as ex:
        print(f"Error in {path_to_db} : {ex}")


if __name__ == '__main__':
    test_db("coffee.db")
