# wallet-balances
Checks all Metamask wallet balances and outputs them to a spreadsheet

1) Download Metamask state logs and save as 'metamask.json' in the same folder

Settings > Advanced > Download State Logs

2) Signup for the debank API and buy some credits

https://cloud.debank.com/dashboard/open-api

Search 'AccessKey' in wallets.py and change to your Debank access key

3) In your console, type:
```
python wallets.py
```

5) The script should output on the console the wallets along with their balances as it writes them to wallets.csv

```
python wallets.py
[u'Shitcoin 1', u'0xxxxxx1', 'Non Hardware', '2023-05-09', 0.7617238258975427, 0]
[u'Ledger 5', u'0xxxxx2', 'Hardware', '2023-05-06', 23.097600516370306, 0]
[u'Shitcoin 2', u'0xxxxx3', 'Non Hardware', '2021-07-09', 36.54599962785208, 0]
```

6) open wallets.csv
