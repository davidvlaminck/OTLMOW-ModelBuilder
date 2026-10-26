from __future__ import annotations


class CouldNotCreateInstanceError(ModuleNotFoundError):
    """
    Exception raised when an instance of a class could not be created.
    """
    def __init__(self, message: str, closest_matches: list[str] | None = None):
        super().__init__(message)
        self.message: str = message
        self.closest_matches: list[str] = closest_matches or []
