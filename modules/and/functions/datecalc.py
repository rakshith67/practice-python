import time
from time import time as my_timer  # use monotonic, perf_counter, process_time
import random

print(time.gmtime(0))
print(time.localtime())
print(time.time())

input("Press ENTER to start")

# wait_time = random.randint(1, 6)
# time.sleep(wait_time)

start_time = my_timer()
input("Press ENTER to end")
end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print("Reaction time is {0}".format(end_time - start_time))

print("The epoch of this system starts at " + time.strftime("%X", time.gmtime(0)))
print("The current timezone is {0} with offset {1}".format(time.tzname[0], time.timezone))

print("local time is " + time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime()))
