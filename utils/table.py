# from module import whateveryouneed 
class Seat:
    def __init__(self, free=False, occupant=None) -> None:
        self.free = free
        self.occupant = occupant

    def set_occupant(self,name:str) -> bool:
        """
        Allows the program to assign someone a seat if its free
        """
        if self.free == True:
            self.occupant = name
            self.free = False
            return True
        else:
            return False

    def remove_occupant(self) -> str:
        """
        remove someone from a seat and return the name of the person occupying the seat before
        """
        if self.free == False:
            prev_occupant = self.occupant
            self.occupant = ""
            self.free = True
            return prev_occupant
        else:
            return "no occupant to remove"
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
    def __str__(self) -> str:
        if self.free == True:
            return "Seat is free"
        else:
            return f'Seat is occupied by {self.occupant}'
        
class Table:
    def __init__(self, capacity:int) -> None:
        self.capacity = capacity
        self.seats = []
        for i in range (0,5):
            self.seats.append(Seat())

    def has_free_spot(self) ->bool:
        """
        returns a bool if a spot is available
        """
        for seat in self.seats:
            if seat.free == True:
                return True
            else:
                return False
        
    def assign_seat(self, name) -> None:
        """
        places someone at the table
        """
        if self.has_free_spot() == True:
            for seat in self.seats:
                if seat.free == True:
                    seat.set_occupant(name)
                    
    def left_capacity(self) -> int:
        """
        returns left seats with an integer
        """
        counter = 0
        for seat in self.seats:
            if seat.free == True:
                counter += 1
        return counter
    def __str__(self) -> str:
        counter = 0
        for seat in self.seats:
            if seat.free == False:
                counter += 1
        return f'Table capacity is {self.capacity} with {counter} seats taken '