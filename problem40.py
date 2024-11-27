'''
y Jane Street.

The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. You should also allow for additional units to be added to the system.

'''


class UnitConverter:
    def __init__(self, base_unit):
        """
        Initialize the UnitConverter with a base unit.
        
        :param base_unit: The base unit to which all other units will be relative.
        """
        self.base_unit = base_unit
        self.units = {base_unit: 1.0}
        self.unit_types = {}  # Optional: to handle different types like length, weight, etc.
    
    def add_unit(self, unit, to_base_factor, unit_type=None):
        """
        Add a new unit with its conversion factor to the base unit.
        
        :param unit: The name of the unit to add.
        :param to_base_factor: The factor to convert from this unit to the base unit.
        :param unit_type: Optional string representing the type/category of the unit.
        """
        if unit in self.units:
            raise ValueError(f"Unit '{unit}' already exists.")
        self.units[unit] = to_base_factor
        if unit_type:
            self.unit_types[unit] = unit_type
    
    def convert(self, quantity, from_unit, to_unit):
        """
        Convert a quantity from one unit to another.
        
        :param quantity: The numerical quantity to convert.
        :param from_unit: The unit of the input quantity.
        :param to_unit: The unit to convert the quantity to.
        :return: The converted quantity.
        """
        if from_unit not in self.units:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        # Optional: Check if both units are of the same type
        if from_unit in self.unit_types and to_unit in self.unit_types:
            if self.unit_types[from_unit] != self.unit_types[to_unit]:
                raise ValueError(f"Cannot convert between different unit types: {from_unit} and {to_unit}")
        
        # Convert from the original unit to the base unit
        quantity_in_base = quantity * self.units[from_unit]
        # Convert from the base unit to the target unit
        converted_quantity = quantity_in_base / self.units[to_unit]
        return converted_quantity

# Example Usage
if __name__ == "__main__":
    converter = UnitConverter("inch")
    
    # Adding length units
    converter.add_unit("foot", 12.0, unit_type="length")       # 1 foot = 12 inches
    converter.add_unit("yard", 36.0, unit_type="length")       # 1 yard = 36 inches
    converter.add_unit("chain", 792.0, unit_type="length")     # 1 chain = 792 inches (22 yards)
    converter.add_unit("mile", 63360.0, unit_type="length")    # 1 mile = 63360 inches (5280 feet)
    converter.add_unit("furlong", 7920.0, unit_type="length")  # 1 furlong = 7920 inches (10 chains)
    
    # Adding weight units (for demonstration)
    converter.add_unit("pound", 1.0, unit_type="weight")       # Assuming pound as base for weight
    converter.add_unit("ounce", 0.0625, unit_type="weight")    # 1 ounce = 0.0625 pounds
    
    # Convert 5 miles to feet
    miles = 5
    feet = converter.convert(miles, "mile", "foot")
    print(f"{miles} miles is {feet} feet.")
    
    # Convert 10 chains to yards
    chains = 10
    yards = converter.convert(chains, "chain", "yard")
    print(f"{chains} chains is {yards} yards.")
    
    # Convert 16 ounces to pounds
    ounces = 16
    pounds = converter.convert(ounces, "ounce", "pound")
    print(f"{ounces} ounces is {pounds} pounds.")
    
    # Attempting invalid conversion between different types
    try:
        converter.convert(1, "mile", "pound")
    except ValueError as e:
        print(e)
