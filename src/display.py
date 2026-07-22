import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

from src.ascii_art import BOMB_STATES, welcome_banner, rule_screen
from src.timer import timer

def rule_book():
    print(Fore.LIGHTCYAN_EX+rule_screen)

def menu():
    print(Fore.LIGHTCYAN_EX+welcome_banner)

def active_bomb():
    print(Fore.LIGHTYELLOW_EX+BOMB_STATES["active"])

def bomb_blast():
    print(Fore.RED+Style.BRIGHT+BOMB_STATES["blast"]+Style.RESET_ALL)

def defused_bomb():
    print(Fore.GREEN+BOMB_STATES["defused"])

def goodbye():
    print(Fore.CYAN+"Thanks for being here...")

