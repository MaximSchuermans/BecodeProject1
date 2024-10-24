from module import whateveryouneed 
class Seat:
    def __init__(self, free:bool, occupant:str ) -> None:
        self.free = free
        self.occupant = occupant
        pass
    def set_occupant(self,name:str) -> None:
        pass
    def remove_occupant(self) -> None:
        pass

class Table:
    def __init__(self, capacity:int)-> None:
        self.capacity = capacity
        self.seats = None
    def has_free_spot(self) ->bool:
        pass
    def assign_seat(self, name) -> None:
        pass
    def left_capacity(self) -> int:
        pass