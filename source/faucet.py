import colorama
from colorama import Fore as fg
import discum
import random
import yaml
import time

with open('config.yaml', 'r+') as file:
    data = yaml.safe_load(file)
    token = data['token']
    address = data['address']
    faucet_channel_id = data['faucet_channel_id']
    allow_author_ids = data['allow_author_ids']
    sui_addresses = data['sui_addresses']


client = discum.Client(token=token, log=False)
colorama.init()


#@client.gateway.command
def on_message(resp):
	if resp.event.message:
		m = resp.parsed.auto()
		if m['author']['id'] in allow_author_ids:
			print(m['content'])


def faucet(address):
	client.sendMessage(faucet_channel_id, f'!faucet {address}')
	

def spam_faucets(address):
	while True:
		wait_time = 30 * 60 + random.randint(5, 207)
		faucet(address)
		now = time.strftime("%I:%M:%S %p", time.localtime()).lstrip('0')
		print(fg.MAGENTA + f'info:' + fg.CYAN + f' [{now}] ' + fg.WHITE + f'faucet successfully initiated to {address}')
		time.sleep(wait_time)
	

if __name__ == '__main__':
    spam_faucets(address=address)