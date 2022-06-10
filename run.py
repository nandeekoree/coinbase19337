import sys
from libs.coinbase import Coinbase
from libs.thread import ThreadPool

def check(email):
    Coinbase(email).run


lists = sys.argv[1]

with open(lists, 'r') as f:
    emails = [i.strip() for i in f.readlines()]

Pool = ThreadPool(3)
for email in emails:
    Pool.add_task(check, email)
Pool.wait_completion()

