import os, sys, platform, ctypes, random, string, requests
from time import sleep
from colorama import Fore

percentage_chance = 0.0000001 # The chance of "finding a wallet"

# Clear console
def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux':
        os.system('clear')
    else:
        print('\n')*120
    return

# Set console title
def setTitle(str):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{str} | CookiesKush420")
    else:
        os.system(f"\033]0;{str}\a")

# Print slow (animation)
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.05)

# Gen random address
def random_string_generator():
    chars = string.ascii_letters + string.digits + string.hexdigits # Added hexdigits to make it seem more like a wallet address
    list = ["bc1", "1", "3"] # Have diffrent starters to look more legit
    start = random.choice(list) # randomly pick the starter
    if start == "bc1": # if starter == bc1 then we change the length of the genned address so there all the same size
        return start + ''.join(random.choice(chars) for x in range(28))
    else:
        return start + ''.join(random.choice(chars) for x in range(30))

# Gen random private key
def random_key_generator():
    chars = string.ascii_letters + string.digits + string.hexdigits
    size = random.randint(45,65)
    return ''.join(random.choice(chars) for x in range(size))

# Gen random wallet balance
def random_balance_generator():
    bal = round(random.uniform(0.001,0.00001), 8)
    return bal

# Convert balance => USD
def BTC_check(bal):
    btc = bal
    r = requests.get("https://blockchain.info/tobtc?currency=USD&value=1")
    result = r.text # Simple code could do with some cleaning up icl
    resultxd = float(btc) / float(result)
    res = int(resultxd)
    output = (str(res) + "$")
    return output

# Write "found" wallets to txt file
def write_address_info(address, bal, worth):
    with open("addressInfo.txt", "a+") as f:
        f.writelines(f"\n----------------------------------------\nAddress: {address}\nBalance: {bal} | {worth}\nPrivate Key: {random_key_generator()}")
    f.close()

# Simple banner
banner = f"""

    {Fore.LIGHTMAGENTA_EX}Welcome to Cookies BTC Stealer
        {Fore.LIGHTBLUE_EX}github.com/callumgm

{Fore.RESET}"""