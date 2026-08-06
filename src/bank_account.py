"""
Bank Account module.

This module contains the BankAccount class which handles
account operations such as deposits, withdrawals, transfers,
and transaction history management.
"""


from src.transaction import Transaction
from src.customer import Customer
from src.exceptions import (
    InvalidAmountError,
    InsufficientBalanceError,
    InvalidAccountDataError
)


class BankAccount:
    """
    Represents a bank account.

    Attributes:
        customer (Customer):
            Customer who owns the account.

        account_number (str):
            Unique account identifier.

        transactions (list[Transaction]):
            List containing account transaction history.
    """

    def __init__(
        self,
        customer: Customer,
        account_number: str,
        balance: float = 0
    ) -> None:
        """
        Initialize a bank account.

        Parameters:
            customer (Customer):
                Account owner.

            account_number (str):
                Unique account number.

            balance (float):
                Initial account balance.

        Raises:
            InvalidAccountDataError:
                If account number is empty or balance is negative.
        """

        if not account_number.strip():

            raise InvalidAccountDataError(
                "Account number cannot be empty!"
            )

        if balance < 0:

            raise InvalidAccountDataError(
                "Initial balance cannot be negative!"
            )

        self.customer = customer
        self.account_number = account_number
        self.__balance = balance
        self.transactions: list[Transaction] = []


    def display_balance(self) -> None:
        """
        Display account information and balance.

        Returns:
            None
        """

        print(f"Customer: {self.customer.name}")
        print(f"Phone: {self.customer.phone}")
        print(
            f"Account Number: "
            f"{self.account_number}"
        )
        print(
            f"Balance: "
            f"${self.__balance:,.0f}"
        )


    def validate_amount(
        self,
        amount: float
    ) -> None:
        """
        Validate transaction amount.

        Parameters:
            amount (float):
                Amount to validate.

        Raises:
            InvalidAmountError:
                If amount is zero or negative.
        """

        if amount <= 0:

            raise InvalidAmountError(
                "Amount must be greater than zero!"
            )


    def deposit(
        self,
        amount: float
    ) -> None:
        """
        Deposit money into account.

        Parameters:
            amount (float):
                Amount to deposit.

        Returns:
            None
        """

        self.validate_amount(amount)

        self.__balance += amount

        transaction = Transaction(
            "Deposit",
            amount
        )

        self.transactions.append(transaction)

        print(
            f"${amount:,.0f} deposited successfully!"
        )


    def withdraw(
        self,
        amount: float
    ) -> None:
        """
        Withdraw money from account.

        Parameters:
            amount (float):
                Amount to withdraw.

        Raises:
            InsufficientBalanceError:
                If balance is insufficient.
        """

        self.validate_amount(amount)

        if amount > self.__balance:

            raise InsufficientBalanceError(
                "Insufficient balance for withdrawal!"
            )

        self.__balance -= amount

        transaction = Transaction(
            "Withdraw",
            amount
        )

        self.transactions.append(transaction)

        print(
            f"${amount:,.0f} withdrawn successfully!"
        )


    def transfer(
        self,
        receiver_account: "BankAccount",
        amount: float
    ) -> None:
        """
        Transfer money to another account.

        Parameters:
            receiver_account (BankAccount):
                Account receiving the money.

            amount (float):
                Amount to transfer.

        Raises:
            InsufficientBalanceError:
                If sender balance is insufficient.
        """

        self.validate_amount(amount)

        if amount > self.__balance:

            raise InsufficientBalanceError(
                "Insufficient balance for transfer!"
            )

        self.__balance -= amount
        receiver_account.__balance += amount

        sender_transaction = Transaction(
            f"Transfer Out to "
            f"{receiver_account.customer.name}",
            amount
        )

        receiver_transaction = Transaction(
            f"Transfer In from "
            f"{self.customer.name}",
            amount
        )

        self.transactions.append(
            sender_transaction
        )

        receiver_account.transactions.append(
            receiver_transaction
        )

        print(
            f"Successfully transferred "
            f"${amount:,.0f} to "
            f"{receiver_account.customer.name}!"
        )


    def display_transactions(self) -> None:
        """
        Display account transaction history.

        Returns:
            None
        """

        print(
            f"\nTransaction History of "
            f"{self.customer.name}:\n"
        )

        if not self.transactions:

            print("No Transaction Found.")

            return

        for transaction in self.transactions:

            transaction.display_transaction()


    def get_balance(self) -> float:
        """
        Return current account balance.

        Returns:
            float:
                Current account balance.
        """

        return self.__balance


    def __str__(self) -> str:
        """
        Return formatted account information.

        Returns:
            str:
                Account details.
        """

        return (
            f"Customer: {self.customer.name}\n"
            f"Phone: {self.customer.phone}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.__balance:,.0f}"
        )


    def to_dict(self) -> dict:
        """
        Convert account data into dictionary format.

        Returns:
            dict:
                Serializable account data.
        """

        return {
            "customer": self.customer.to_dict(),
            "account_number": self.account_number,
            "balance": self.__balance,
            "transactions": [
                transaction.to_dict()
                for transaction in self.transactions
            ]
        }