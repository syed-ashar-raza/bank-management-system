class InsufficientBalanceError(Exception):
    """Raised when an account does not have enough balance."""
    pass


class AccountNotFoundError(Exception):
    """Raised when an account cannot be found."""
    pass


class InvalidAmountError(Exception):
    """Raised when an amount is invalid."""
    pass

class DuplicateAccountError(Exception):
    """Raised when an account number already exists."""
    pass

class InvalidCustomerDataError(Exception):
    """Raised when customer information is invalid."""
    pass


class InvalidAccountDataError(Exception):
    """Raised when bank account information is invalid."""
    pass