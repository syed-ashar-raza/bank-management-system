"""
Transaction module.

This module contains the Transaction class which represents
financial transactions performed on bank accounts.
"""


from datetime import datetime


class Transaction:
    """
    Represents a bank transaction.

    Attributes:
        transaction_type (str):
            Type or description of the transaction.

        amount (float):
            Amount involved in the transaction.

        date (str):
            Date and time when the transaction occurred.
    """

    def __init__(
        self,
        transaction_type: str,
        amount: float
    ) -> None:
        """
        Initialize a Transaction object.

        Parameters:
            transaction_type (str):
                Description of the transaction.

            amount (float):
                Transaction amount.
        """

        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now().strftime(
            "%d-%m-%Y %I:%M:%S %p"
        )


    def display_transaction(self) -> None:
        """
        Display transaction details.

        Returns:
            None
        """

        print("----------------------------")
        print(
            f"Transaction Type: "
            f"{self.transaction_type}"
        )
        print(
            f"Amount: ${self.amount:,.0f}"
        )
        print(
            f"Date: {self.date}"
        )
        print("----------------------------")


    def __str__(self) -> str:
        """
        Return a formatted string representation
        of the transaction.

        Returns:
            str:
                Formatted transaction details.
        """

        return (
            f"Transaction Type: {self.transaction_type}\n"
            f"Amount: ${self.amount:,.0f}\n"
            f"Date: {self.date}"
        )


    def to_dict(self) -> dict[str, str | float]:
        """
        Convert transaction data into a dictionary.

        Returns:
            dict[str, str | float]:
                Dictionary containing transaction details.
        """

        return {
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "date": self.date
        }