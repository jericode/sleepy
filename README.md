# Sleepy Program

## Intro
My name is Micah Mitchell and i am 15 yrs. old and this is my 
first program. I did this project with my older brother
Josh as he was teaching me to program.

## What the program does.
The sleepy program was designed to keep the 
azure server awake which is located in the 
azure cloud. The free azure servers fall asleep every 20 min.
to conserve resources. So this program was written to
auto load the site every ten min. and keep the site warm.  



## How the program works
the program is written in python and makes a get request to
https://avalearner2.azurewebsites.net using the requests
library. it then prints the status code and page content to
the console.


## How to set it up
the site was made to run on a raspberry pi and be called 
from a cron job. To run the program call 
```bash
python wakeup.py
```
to call this from cron type this command
```bash
crontab -e
```

add this line to the cron file
```bash
*/10 * * * * python /home/pi/sleepy/wakeup.py
``` 
this will run the program every ten minutes.