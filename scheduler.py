import schedule
import time
import os
def job():
    print("\n Running automated analytics pipeline\n")
    os.system("python main.py")

#Fixing Schedule
schedule.every(10).seconds.do(job)
print("Scheduler Started")

while True:
    schedule.run_pending()
    time.sleep(1)