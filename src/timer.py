import time
from colorama import Fore, Style

def show_timer(time_remaining):

    for remaining in range(time_remaining , -1, -1):

        mins, secs = divmod(remaining, 60)

        timer_format=f"{mins:02d}:{secs:02d}"
        print(Fore.RED+ Style.BRIGHT+f"\r||{timer_format}||"+Style.RESET_ALL, end="")
        time.sleep(1)
    
    print("BLAST! BLAST! BLAST!")


        
