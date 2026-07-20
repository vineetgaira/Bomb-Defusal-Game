import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

from src.ascii_art import BOMB_STATES, welcome_banner, rule_screen



def rule_book():
    print(Fore.CYAN+rule_screen)

def menu():
    print(Fore.CYAN+welcome_banner)

def active_bomb():
    print(Fore.LIGHTYELLOW_EX+BOMB_STATES["active"])

def bomb_blast():
    print(Fore.RED+BOMB_STATES["blast"])

def defused_bomb():
    print(Fore.GREEN+BOMB_STATES["defused"])