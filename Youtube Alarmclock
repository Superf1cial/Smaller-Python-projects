import webbrowser
import datetime
import random
import time

t = time.strftime("%H:%M")
print(t)

Alarm = input("Enter a time you want to get a alarm for(use this format: 17:13 (hh:mm):")

with open("youtubelinks.txt") as f:
    content = f.readlines()

while t != Alarm:
    t = time.strftime("%H:%M")
    time.sleep(1)
    print (t)

if t == Alarm:
    print("It's time to wake up and go home brothah")
    random_video = random.choice(content)
    webbrowser.open(random_video)

