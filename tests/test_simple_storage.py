from brownie import accounts, SimpleStorage


def testing():
    # arrange
    account = accounts[0]

    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    initial_value = simple_storage.retrieve()
    expected = 0
    # assert
    assert initial_value == expected


def test_update():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    value = 11
    simple_storage.store(value, {"from": account})
    updated_value = simple_storage.retrieve()
    # assert
    assert updated_value == value
