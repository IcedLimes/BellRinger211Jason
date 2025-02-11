import time 
hour_end=14 
minute_end = 19 

while True:
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time. tm_min 
    remaining_minutes = (hour_end - current_hour) * 60 + (minute_end - current_minute)
    print(f"Time remaining until class ends: {remaining_minutes} minutes")
