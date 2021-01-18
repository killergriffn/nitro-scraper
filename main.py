import requests
from termcolor import cprint, colored
import os, sys
import random
import string
import ctypes

if sys.platform.startswith('win32'):
	ctypes.windll.kernel32.SetConsoleTitleW("Discord Nitro Generator + Checker || By NAVI1237")
	clear = lambda: os.system('cls')
elif sys.platform.startswith('linux'):
	sys.stdout.write("\x1b]2;Discord Nitro Generator + Checker || By NAVI1237\x07")
	clear = lambda: os.system('clear')
else:
    print('Sorry, unsuported system :(')
    exit()
  
clear()
cprint('Discord Nitro Generator + Checker\n', 'yellow', attrs=['bold'])

try:
	amount = int(input(colored('How much codes will be generated: ', 'green', attrs=['bold'])))
except:
	cprint('Invalid option', 'red', attrs=['bold'])
	exit()

nitro_type = input(colored('Boost or Classic: ', 'green', attrs=['bold']))
if nitro_type != 'boost' and nitro_type != 'classic':
	cprint('Invalid option', 'red', attrs=['bold'])
	exit()
	
use_checker = input(colored('Enable checker? (Y/N) ', 'green', attrs=['bold'])).lower()
if use_checker == 'y':
	use_checker = True
elif use_checker == 'n':
	use_checker = False
else:
	cprint('Invalid option', 'red', attrs=['bold'])
	exit()

if use_checker:
	use_proxies = input(colored('Use proxies? (Y/N) ', 'green', attrs=['bold'])).lower()
	if use_proxies == 'y':
		use_proxies = True
		proxies_list = open('proxies.txt').read().splitlines()
		ratelimited_proxies = []
	elif use_proxies == 'n':
		use_proxies = False
	else:
		cprint('Invalid option', 'red', attrs=['bold'])
		exit()

nitro_codes = open('NitroCodes.txt', 'w')
nitro_codes.write('')
nitro_codes.close()
nitro_codes = open('NitroCodes.txt', 'a')

if not use_checker:
	cprint('Generating...', 'blue')
	for x in range(amount):
		if nitro_type == 'boost':
			code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
		else:
			code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
		nitro_codes.write(f"discord.gift/{code}\n")
else:
	cprint('Generating...', 'blue')
	for x in range(amount):
		if nitro_type == 'boost':
			code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
		else:
			code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
			
		try:
			if use_proxies:
				index = random.randint(0, len(proxies_list) - 1)
				proxy = proxies_list[index]
				proxies = {
					"http": proxy
				}
				req = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}", proxies=proxies, timeout=3)
				if req.status_code == 200:
					cprint(f'Working code: discord.gift/{code}', 'yellow', attrs=['bold'])
					nitro_codes.write(f'discord.gift/{code}\n')
				elif req.status_code == 404:
					cprint(f'Invalid code: discord.gift/{code}', 'red', attrs=['bold'])
				elif req.status_code == 429:
					cprint(f'{proxy} is rate limited!', 'red', attrs=['bold'])
					ratelimited_proxies.append(proxies_list[index])
					del proxies_list[index]
                    if len(proxies_list) == 0:
			        for p in ratelimited_proxies:
			            proxies_list.append(p)
			        del ratelimited_proxies
			        ratelimited_proxies = []
			else:
				req = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}", timeout=3)
				if req.status_code == 200:
					cprint(f'Working code: discord.gift/{code}', 'yellow', attrs=['bold'])
					nitro_codes.write(f'discord.gift/{code}\n')
		except Exception as e:
			cprint(e, 'red', attrs=['bold'])