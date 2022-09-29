
import time
from playsound import playsound 



def countdown(time_sec):
    
    while time_sec:
        
        mins,secs=divmod(time_sec,60)
        timeformat='{:01d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1)
        
        time_sec-=1
        
       
     
times=00
for i in range(3):
   
    print(times)
    times+=1
    countdown(5)
      
    playsound("jhum.mp3")  

