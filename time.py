import time
hour_end=14
minute_end = 19

while True:
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time. tm_min
    remaining_hours = hour_end - current_hour
    remaining_minutes = minute_end -current_minute

    if remaining_minutes < 0:
        remaining_hours -= 1
        remaining_minutes += 60
    print(f"Time remaining until class ends: {remaining_hours} hours and {remaining_minutes} minutes")
