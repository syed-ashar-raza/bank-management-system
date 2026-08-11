from src.bank_account import BankAccount
from src.customer import Customer
from src.exceptions import (
    InvalidAmountError,
    InsufficientBalanceError,
)

def create_test_account():

    customer = Customer(
        "Ashar Raza",
        "03476371697"
    )

    return BankAccount(
        customer,
        "ACC101",
        5000
    )


def test_account_creation():

    account = create_test_account()

    assert account.account_number == "ACC101"
    assert account.get_balance() == 5000


def test_deposit():

    account = create_test_account()

    account.deposit(2000)

    assert account.get_balance() == 7000

def test_withdraw():

    account = create_test_account()

    account.withdraw(2000)

    assert account.get_balance() == 3000

def test_invalid_deposit():

    account = create_test_account()

    try:
        account.deposit(-100)

    except InvalidAmountError:
        assert True

    else:
        assert False

def test_insufficient_balance():

    account = create_test_account()

    try:
        account.withdraw(10000)

    except InsufficientBalanceError:
        assert True

    else:
        assert False

def test_transfer():

    sender = create_test_account()
    receiver = BankAccount(
        Customer(
            "Receiver",
            "03000000000"
        ),
        "ACC102",
        2000
    )

    sender.transfer(receiver, 1000)

    assert sender.get_balance() == 4000
    assert receiver.get_balance() == 3000

def test_search_transactions():
    account = create_test_account()

    account.deposit(2000)

    results = account.search_transactions("Deposit")

    assert len(results) == 1
    assert results[0].transaction_type == "Deposit"
    assert results[0].amount == 2000

def test_search_transactions_case_insensitive():
    account = create_test_account()

    account.deposit(2000)

    results = account.search_transactions("deposit")

    assert len(results) == 1
    assert results[0].transaction_type == "Deposit"

def test_search_transactions_no_match():
    account = create_test_account()

    account.deposit(2000)

    results = account.search_transactions("Withdraw")

    assert results == []