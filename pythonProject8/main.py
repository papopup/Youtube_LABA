
calculation_to_units = 24
name_of_units = 'hours'

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
    elif num_of_days == 0:
        print('your entered number is  0 ! please enter positive number')

def check_and_count(days_number_elem):
    try:

        user_input_number = int(days_number_elem)
        if user_input_number >0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print('your entered number is  0 ! please enter positive number')
        else:
            print('your entered negative number ! please enter positive number')

    except ValueError:
        print('you input is not a useful number or input is a text')

user_input = ''
while user_input != 'exit' and user_input != 'EXIT' and user_input != 'Exit':
    user_input = input('Please enter a number of dates for convertizing to hours! it can also be entered as list coma sepated. \n')

    for days_number_elem in user_input.split():
        check_and_count(days_number_elem)
