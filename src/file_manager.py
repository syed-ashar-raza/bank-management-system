"""
File Manager module.

This module handles saving and loading bank account data
using JSON file storage.
"""

import json
from pathlib import Path

from src.bank_account import BankAccount
from src.customer import Customer
from src.transaction import Transaction


BASE_DIR = Path(__file__).resolve().parent.parent
FILE_NAME = BASE_DIR / "data" / "accounts.json"


class FileManager:
    """
    Handles saving and loading bank account data.
    """

    @staticmethod
    def save_accounts(
        accounts: dict[str, BankAccount],
        file_name: Path = FILE_NAME,
    ) -> bool:
        """
        Save bank accounts to a JSON file.

        Returns:
            bool:
                True if saving succeeds, otherwise False.
        """

        data = [
            account.to_dict()
            for account in accounts.values()
        ]

        try:
            file_name.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            with open(
                file_name,
                "w",
                encoding="utf-8",
            ) as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                )

            return True

        except OSError as error:
            print(
                f"Error saving accounts to "
                f"{file_name}: {error}"
            )
            return False

    @staticmethod
    def load_accounts(
        file_name: Path = FILE_NAME,
    ) -> list[BankAccount]:
        """
        Load bank accounts from a JSON file.

        Returns:
            list[BankAccount]:
                Reconstructed accounts, or an empty list if
                the file does not exist or contains invalid JSON.
        """

        try:
            with open(
                file_name,
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

            return FileManager.create_accounts(data)

        except json.JSONDecodeError:
            print(
                "Warning: accounts.json is corrupted. "
                "Starting with empty accounts."
            )
            return []

        except FileNotFoundError:
            print(
                f"Warning: {file_name} not found. "
                "Starting with empty accounts."
            )
            return []

    @staticmethod
    def create_accounts(
        data: list[dict],
    ) -> list[BankAccount]:
        """
        Convert JSON data into BankAccount objects.
        """

        accounts: list[BankAccount] = []

        for account_data in data:
            customer_data = account_data["customer"]

            customer = Customer(
                customer_data["name"],
                customer_data["phone"],
            )

            account = BankAccount(
                customer,
                account_data["account_number"],
                account_data["balance"],
            )

            for transaction_data in account_data.get(
                "transactions",
                [],
            ):
                transaction = Transaction(
                    transaction_data["transaction_type"],
                    transaction_data["amount"],
                )

                account.transactions.append(transaction)

            accounts.append(account)

        return accounts
