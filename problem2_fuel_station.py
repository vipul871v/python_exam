class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        """
        Initializes the fuel station with the given number of slots for each type.
        """
        self.capacity = {"diesel": diesel, "petrol": petrol, "electric": electric}
        self.occupied = {"diesel": 0, "petrol": 0, "electric": 0}

    def fuel_vehicle(self, fuel_type: str) -> bool:
        """
        Attempts to fuel a vehicle of the given type.

        Args:
        fuel_type (str): The type of fuel required (diesel, petrol, electric).

        Returns:
        bool: True if the vehicle is successfully fueled, False otherwise.
        """
        if fuel_type not in self.capacity:
            raise ValueError(f"Invalid fuel type: {fuel_type}")

        if self.occupied[fuel_type] < self.capacity[fuel_type]:
            self.occupied[fuel_type] += 1
            return True
        return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        """
        Frees a slot of the given fuel type for future use.

        Args:
        fuel_type (str): The type of fuel slot to free (diesel, petrol, electric).

        Returns:
        bool: True if a slot was successfully freed, False otherwise.
        """
        if fuel_type not in self.capacity:
            raise ValueError(f"Invalid fuel type: {fuel_type}")

        if self.occupied[fuel_type] > 0:
            self.occupied[fuel_type] -= 1
            return True
        return False
