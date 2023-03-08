

def days_to_units(num_of_days, conversion_units):
    if conversion_units == 'hours':
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_units == 'minutes':
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def check_and_count(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["units"])
            print(calculated_value)
        elif user_input_number == 0:
            print('your entered number is  0 ! please enter positive number')
        else:
            print('your entered negative number ! please enter positive number')

    except ValueError:
        print('you input is not a useful number or input is a text')


user_input_message = "Please enter a number of dates for convertizing UNITS! colon separated. \n"
