from brownie import SimpleStorage,config,network,accounts

def deploy_simple_storage():
    account= get_account()
    simple_storage= SimpleStorage.deploy({"from":account})
    default_value=simple_storage.retrieve()
    print("the default value is : ", default_value)
    store_tx=simple_storage.store(11,{"from":account})
    store_tx.wait(1)

    print("the current stored value is : ",simple_storage.retrieve())


def get_account():
    if network.show_active()=="development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()