"""Constants used by Domum."""

MAJOR_VERSION = 0  # MAJOR version when you make API changes
MINOR_VERSION = 1  # MINOR version when you add new functionality
PATCH_VERSION = 0  # PATCH version when you make backwards compatible bug fixes

__version__ = f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"

REQUIRED_PYTHON_VERSION = (3, 8, 0)

NAME = "Domum"

# Themes
THEME_DARK = "dark"
THEME_LIGHT = "light"

# System of measurement
UNIT_SYSTEM = "unit_system"
UNIT_SYSTEM_IMPERIAL = "imperial"
UNIT_SYSTEM_METRIC = "metric"

# Degree unit
DEGREE = "°"
 
# Temperature units
TEMPERATURE_CELSIUS = f"{DEGREE}C"
TEMPERATURE_FAHRENHEIT = F"{DEGREE}F"
TEMPERATURE_KELVIN = F"{DEGREE}K"

# Length units
LENGTH = "length"
LENGTH_INCHES = "in"
LENGTH_FEET = "ft"
LENGTH_YARDS = "yd"
LENGTH_MILES = "mi"

LENGTH_MILLIMETERS = "mm"
LENGTH_CENTIMETERS = "cm"
LENGTH_METERS = "m"
LENGTH_KILOMETERS = "km"

# Mass units
MASS = "mass"
MASS_OUNCE = "oz"
MASS_POUNDS = "lb"

MASS_GRAMS = "g"

# Volume units
VOLUME = "volume"
VOLUME_GALLONS = "gal"

VOLUME_LITERS = "L"