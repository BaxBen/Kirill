import datetime as dt
import time

now = dt.datetime.now()
slep_time = time.sleep(2)
now_sleep = dt.datetime.now()
time_raz = now_sleep - now
print(time_raz)