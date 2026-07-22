import time
from colorama import Fore, Style
TOTAL_SECONDS = 60

def timer():

    for remaining in range(TOTAL_SECONDS, -1, -1):

        mins, secs = divmod(remaining, 60)

        timer_format=f"{mins:02d}:{secs:02d}"
        print(Fore.RED+ Style.BRIGHT+f"\r||{timer_format}||"+Style.RESET_ALL, end="")
        time.sleep(1)
    
    print("BLAST! BLAST! BLAST!")


        
