from table.py import Table
from typing import List

class Openspace:

    def __init__(self, tables: List[Tabel], names: List[str], number_of_tables=6) -> None:
        self.tables: List[Table] = [Table() for i in range(0, number_of_tables + 1)]
        self.number_of_tables: int = number_of_tables
        self.seated: List[str] = []
        self.usneated: List[str] = [person for person in names]

    def organize(self) -> None:
        """
        Randomly assigns people to Seat object in the different Table objects.
        """
        # If number of people is equal or more than 24 distribute 24 people randomly over the 4 tables
        # and add the rest to a list
        if len(self.unseated) >= 24:
            for table in self.tables:
                for i in range(0, 7):
                    person = rand.choice(self.unseated)
                    # Update the lists of seated and unseated people
                    self.update_seats(person, table)
        elif len(self.unseated) % 6 != 1:
            # Fill the tables with 6 people such that there will be no table with only 1 peron
            while len(self.unseated) != 0:
                for table in self.tables:
                    if table.left_capacity == 0:
                        continue
                    person = rand.choice(self.unseated)
                    self.update_seats(person, table)
                    

    def update_seats(self, name, table):
        # Update internal state to keep track of seated and unseated people
        # Should be a private method
        self.unseated.remove(name)
        self.seated.append(name)
        table.assign_seat(name)

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
