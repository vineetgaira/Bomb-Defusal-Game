import time

TOTAL_SECONDS = 60

def timer():

    for remaining in range(TOTAL_SECONDS, -1, -1):

        mins, secs = divmod(remaining, 60)

        timer_format=f"{mins:02d}:{secs:02d}"
    
        return timer_format



        
