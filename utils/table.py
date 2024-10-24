# from module import whateveryouneed 
class Seat:
    def __init__(self, free:bool, occupant:str ) -> None:
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
        
class Table:
    def __init__(self, capacity:int) -> None:
        self.capacity = capacity
        self.seats = list_of_seat_objects

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
        if self.has_free_spot(self) == True:
            for seat in self.seats:
                if seat.free == True:
                    seat.set_occupant(name)
                    

    def left_capacity(self) -> int:
        """
        returns left seats with an integer
        """
        counnter = 0
        for seat in self.seats:
            if seat.free == True:
                counter += 1
        return counter
