from datetime import datetime

import csv
import json
import os
import requests
import time


path_for_metamask = os.getcwd() + '/metamask.json'
wallet_csv = open('wallets.csv', 'w')
writer = csv.writer(wallet_csv)
header = ['Name', 'Address', 'Wallet Type', 'Last Accessed', 'Balance', 'Claimable Items']
writer.writerow(header)

request_header = {
	'accept': 'application/json',
	'AccessKey': ''
}

count = 0
with open(path_for_metamask) as metamask_data:
	metamask_data = json.load(metamask_data)
	wallets = metamask_data['metamask']['identities']
	hw_wallets = set()

	for keyring in metamask_data['metamask']['keyrings']:
		if 'Hardware' in keyring['type']:
			hw_wallets.update(keyring['accounts'])


	for _, wallet in wallets.iteritems():
		name = wallet['name']
		address = wallet['address']
		wallet_type = 'Hardware' if address in hw_wallets else 'Non Hardware'
		
		last_selected = datetime.fromtimestamp(float(wallet['lastSelected'])/1000.0)
		last_selected_formatted = last_selected.strftime('%Y-%m-%d')

		response = requests.get('https://pro-openapi.debank.com/v1/user/total_balance?id={address}'.format(address=address), headers=request_header)
		balance = json.loads(response.text)['total_usd_value']

		data = [name, address, wallet_type, last_selected_formatted, balance, 0]
		print (data)

		writer.writerow(data)
		
		count += 1
		if count == 99:
			print "Debank API Rate Limit ..."
			count = 0
			time.sleep(1)