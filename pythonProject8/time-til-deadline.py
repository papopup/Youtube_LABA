import datetime

user_input = input("enter your goal with a deadline separeted by colon \n ")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

dead_line_date = (datetime.datetime.strptime(deadline, "%d.%m.%Y"))
today_date = datetime.datetime.today()
time_till = (dead_line_date - today_date)

print(f"Time remaining {goal} is {time_till.days}")
