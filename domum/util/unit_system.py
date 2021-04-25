"""
Unit system class and methods.
"""

from domum.const import (
    UNIT_SYSTEM,
    UNIT_SYSTEM_IMPERIAL,
    UNIT_SYSTEM_METRIC,
    TEMPERATURE_CELSIUS,
    TEMPERATURE_FAHRENHEIT,
    LENGTH_METERS,
    LENGTH_MILES,
    MASS_GRAMS,
    MASS_POUNDS,
    VOLUME_GALLONS,
    VOLUME_LITERS
)


def validate_unit():
    pass


class UnitSystem:
    """
    A holder for units of measurement.
    """

    __slots__ = [
        "name",
        "temperature",
        "length",
        "mass",
        "volume"
    ]

    def __init__(
        self,
        name: str,
        temperature: str,
        length: str,
        mass: str,
        volume: str
    ) -> None:
        """
        Initialize a new unit system object.
        """

        self.name = name
        self.temperature = temperature
        self.length = length
        self.mass = mass
        self.volume = volume

    def __repr__(self) -> str:
        """
        Return the representation.
        """

        args = [
            "name={}".format(self.name),
            "temperature={}".format(self.temperature),
            "length={}".format(self.length),
            "mass={}".format(self.mass),
            "volume={}".format(self.volume),
        ]
        
        return "<{} {}>".format(type(self).__name__, ", ".join(args))

    def as_dict(self) -> dict:
        """
        Return dict representation of unit system.
        """

        return {
            "name": self.name,
            "temperature": self.temperature,
            "length": self.length,
            "mass": self.mass,
            "volume": self.volume
        }


IMPERIAL_SYSTEM = UnitSystem(
    name=UNIT_SYSTEM_IMPERIAL,
    temperature=TEMPERATURE_FAHRENHEIT,
    length=LENGTH_MILES,
    mass=MASS_POUNDS,
    volume=VOLUME_GALLONS
)

METRIC_SYSTEM = UnitSystem(
    name=UNIT_SYSTEM_METRIC,
    temperature=TEMPERATURE_CELSIUS,
    length=LENGTH_METERS,
    mass=MASS_GRAMS,
    volume=VOLUME_LITERS
)
