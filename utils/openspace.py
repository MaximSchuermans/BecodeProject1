from table.py import Table
from typing import List

class Openspace:

    def __init__(self, tables: List[Tabel], number_of_tables=4) -> None:
        self.tables: List[Table] = None
        self.number_of_tables: int = None

    def organize(self, names: List[str]) -> None:
        """
        Randomly assigns people to Seat object in the different Table objects.
        """
        pass

    def display(self) -> None:
        """
        Display the different tables and their occupants in a nice and readable way.
        """
        pass

    def store(self, filename: str) -> None:
        """
        Stores the repartition in an excel file.
        """
        pass

    def __str__(self) -> str:
        """
        Returns the string representation of this object
        """
        pass
