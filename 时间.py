import datetime
import os

print(datetime.datetime.now())

#while True:
nowtime = datetime.datetime.now()
ti = nowtime.second

print(ti)
os.system("shutdown -s")