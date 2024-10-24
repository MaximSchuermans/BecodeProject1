from table import Table
from typing import List

class Openspace:

    def __init__(self, tables: List[Table], number_of_tables=4) -> None:
        self.tables: List[Table] = None
        self.number_of_tables: int = None

    def organize(self, names: List[str]) -> None:
        """
        Randomly assigns people to Seat object in the different Table objects.
        """
        pass

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
