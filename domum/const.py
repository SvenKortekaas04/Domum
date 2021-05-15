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

# Data units
DATA_BYTES = "B"
DATA_KILOBYTES = "kB"
DATA_MEGABYTES = "MB"
DATA_GIGABYTES = "GB"
DATA_TERABYTES = "TB"