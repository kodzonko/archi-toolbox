"""Architecture-related exceptions."""


class InputError(Exception):
    """Exception raised for errors in the user input or user environment."""

    @classmethod
    def plan_load_failed(cls, file: object) -> InputError:
        """Build an error for a plan file that could not be loaded."""
        return cls(f"Could not load the plan from file: {file}.")
