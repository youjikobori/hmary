from aiogram import Bot, Dispatcher, html
import os
from dotenv import load_dotenv
import getpass
from pydantic import ConfigDict

import version_checker

#config .env
load_dotenv()

BOT_TOKEN=os.getenv('BOT_TOKEN')
LOGO="../assets/logo.txt"

# Func: clear-the-terminal
def clearTerminal():
	os.system('cls' if os.name == 'nt' else 'clear')

# Func: print-the-logo
def logo(file=LOGO):
    try:
        print(open(file, encoding='utf-8').read())
    except:
        print(f'"{file}" not found\n')

clearTerminal()

# Main:
def main():
	logo()
	version_checker.check_version()
	print(' ')
	choice=input(' >> ')

if __name__ == '__main__':
	main()

getpass.getpass('\nThe program has finished running.\nPress [ENTER] to continue\n')
