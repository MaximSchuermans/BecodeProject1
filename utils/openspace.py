#from table.py import Table
from .table import Table
#from . import table
#from ./table import Table
from typing import List

class Openspace:

    def __init__(self, names: List[str], number_of_tables=6) -> None:
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
        for table_number, table in enumerate(self.tables, start=1):
            print(f"Table {table_number}:")
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant == True else "Empty"
                print(f"  Seat: {occupant}")
            print()

    def store(self, filename: str) -> None:
        """
        Stores the repartition in an Excel file.
        """
        data = []
        for table_number, table in enumerate(self.tables, start=1):
            for seat_number, seat in enumerate(table.seats, start=1):
                occupant = seat.occupant if seat.occupant == True else "Empty"
                data.append({
                    "Table": table_number,
                    "Seat": seat_number,
                    "Occupant": occupant
                })
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)    
        pass

    def __str__(self) -> str:
        """
        Returns the string representation of this object
        """
        output = []
        for table_number, table in enumerate(self.tables, start=1):
            output.append(f"Table {table_number}:")
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant else "Empty"
                output.append(f"  Seat: {occupant}")
            output.append("") 
        return "\n".join(output)
