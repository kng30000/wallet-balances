# wallet-balances
Checks all Metamask wallet balances and outputs them to a spreadsheet

1) Download Metamask state logs and save as 'metamask.json'

Settings > Advanced > Download State Logs

2) Signup for the debank API and buy some credits

https://cloud.debank.com/dashboard/open-api

Search 'AccessKey' in wallets.py and change to your Debank access key

    python wallets.py
