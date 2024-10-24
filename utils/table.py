from module import whateveryouneed 

class Seat:
    def __init__(self, free:bool, occupant:str ) -> None:
        self.free = free
        self.occupant = occupant

    def set_occupant(self,name:str) -> None:
        """
        Allows the program to assign someone a seat if its free
        """
        pass

    def remove_occupant(self) -> None:
        """
        remove someone from a seat and return the name of the person occupying the seat before
        """
        pass

class Table:
    def __init__(self, capacity:int)-> None:
        self.capacity = capacity
        self.seats = None

    def has_free_spot(self) ->bool:
        """
        returns a bool if a spot is available
        """
        pass

    def assign_seat(self, name) -> None:
        """
        places someone at the table
        """
        pass

    def left_capacity(self) -> int:
        """
        returns left seats with an integer
        """
        pass
