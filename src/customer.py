"""
Customer module.

This module contains the Customer class which represents
a bank customer and provides customer-related operations.
"""


from src.exceptions import InvalidCustomerDataError


class Customer:
    """
    Represents a bank customer.

    Attributes:
        name (str):
            Customer's full name.

        phone (str):
            Customer's phone number.
    """

    def __init__(self, name: str, phone: str) -> None:
        """
        Initialize a Customer object.

        Parameters:
            name (str):
                Customer's full name.

            phone (str):
                Customer's phone number.

        Raises:
            InvalidCustomerDataError:
                If name is empty or phone contains non-digit characters.
        """

        if not name.strip():

            raise InvalidCustomerDataError(
                "Customer name cannot be empty!"
            )

        if not phone.isdigit():

            raise InvalidCustomerDataError(
                "Phone number must contain only digits!"
            )

        self.name = name
        self.phone = phone


    def display_customer(self) -> None:
        """
        Display customer information.

        Returns:
            None
        """

        print(f"Customer: {self.name}")
        print(f"Phone: {self.phone}")


    def __str__(self) -> str:
        """
        Return a string representation of the customer.

        Returns:
            str:
                Formatted customer information.
        """

        return (
            f"Customer: {self.name}, "
            f"Phone: {self.phone}"
        )


    def to_dict(self) -> dict[str, str]:
        """
        Convert customer data into a dictionary.

        Returns:
            dict[str, str]:
                Dictionary containing customer information.
        """

        return {
            "name": self.name,
            "phone": self.phone
        }