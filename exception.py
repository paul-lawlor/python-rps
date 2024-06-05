"""Simple custom exception to provide an error message for an invalid option"""


class InvalidOptionError(Exception):
    """Simple custom exception to provide an error message for an invalid option"""

    def cause_error(self):
        """Simple custom exception to provide an error message for an invalid option"""
        raise InvalidOptionError(
            """That is an invalid option!
            Please select either:
                            1. Rock
                            2. Paper
                            3. Scissors\n"""
        )
