"""Cloud Drive Fuser exception classes."""


class PearsonnetError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg


class PearsonnetConfigError(PearsonnetError):
    """Config related errors."""
    pass


class PearsonnetRuntimeError(PearsonnetError):
    """Generic runtime errors."""
    pass


class PearsonnetArgumentError(PearsonnetError):
    """Argument related errors."""
    pass
