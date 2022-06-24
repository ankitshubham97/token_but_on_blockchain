from scripts.helper import get_account, deploy_mocks
from brownie import Ankit0Token, MockV3Aggregator, network


def deploy_ankit0_token(account, initial_supply):
  print(f'Deploying from account {account} with initial_supply {initial_supply} ...')
  ankit0_token = Ankit0Token.deploy(initial_supply, {"from": account})
  print(f"Contract deployed to {ankit0_token.address}")
  return ankit0_token

def main():
  if network.show_active() != "ganache-local":
    sys.exit("Only ganache-local network is supported.")
  account = get_account()
  deploy_mocks()
  initial_supply = 1000 * 10**18
  ankit0_token = deploy_ankit0_token(account, initial_supply)

