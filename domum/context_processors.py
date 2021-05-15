from typing import (
    Any,
    Dict
)

from domum import const


def main(request) -> Dict[str, Any]:
    return {
        "const": const
    }