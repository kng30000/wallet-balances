import os
import json
import requests
import csv
from datetime import datetime

METAMASK_JSON_PATH = os.path.join(os.getcwd(), 'metamask.json')
WALLETS_CSV_PATH = 'wallets.csv'
DEBANK_API_ENDPOINT = 'https://pro-openapi.debank.com/v1/user/total_balance'
REQUEST_HEADER = {
    'accept': 'application/json',
    'AccessKey': ''
}


def get_wallet_balance(address):
    response = requests.get(f'{DEBANK_API_ENDPOINT}?id={address}', headers=REQUEST_HEADER)
    return json.loads(response.text)['total_usd_value']


def export_wallet_data_to_csv():
    with open(METAMASK_JSON_PATH, 'r') as metamask_file, open(WALLETS_CSV_PATH, 'w', newline='') as wallet_csv:
        metamask_data = json.load(metamask_file)
        wallets = metamask_data['metamask']['identities']

        hw_wallets = set()
        for keyring in metamask_data['metamask']['keyrings']:
            if 'Hardware' in keyring['type']:
                hw_wallets.update(keyring['accounts'])

        writer = csv.writer(wallet_csv)
        header = ['Name', 'Address', 'Wallet Type', 'Last Accessed', 'Balance', 'Claimable Items']
        writer.writerow(header)

        rate_limit_counter = 0
        for _, wallet in wallets.items():
            name = wallet['name']
            address = wallet['address']
            wallet_type = 'Hardware' if address in hw_wallets else 'Non-Hardware'
            last_selected = datetime.fromtimestamp(float(wallet['lastSelected']) / 1000.0)
            last_selected_formatted = last_selected.strftime('%Y-%m-%d')
            balance = get_wallet_balance(address)

            data_row = [name, address, wallet_type, last_selected_formatted, balance, 0]
            print(data_row)
            writer.writerow(data_row)

            rate_limit_counter += 1
            if rate_limit_counter == 99:
                print("Debank API Rate Limit ...")
                rate_limit_counter = 0
                time.sleep(1)


if __name__ == '__main__':
    export_wallet_data_to_csv()
