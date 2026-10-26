from __future__ import annotations


class InvalidOptionError(ValueError):
    """
    Exception raised when an invalid option is provided.
    """

    def __init__(self, message: str, closest_matches: list[str] | None = None):
        super().__init__(message)
        self.message: str = message
        self.closest_matches: list[str] = closest_matches or []
