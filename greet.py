import time

# print(time.localtime().tm_hour)
curr_time = time.localtime().tm_hour
# print(curr_time)
if curr_time >= 4 and curr_time < 12:
    print("Good Morning")
elif curr_time >=12 and curr_time < 4:
    print("Good Afternoon")
elif curr_time >= 4 and curr_time < 22:
    print("Good Evening")
elif curr_time >= 22 and curr_time < 24:
    print("Good Night")