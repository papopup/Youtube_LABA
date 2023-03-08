from helper import check_and_count, user_input_message

user_input = ""
while user_input != 'exit':
    user_input = input(user_input_message)
    days_and_units = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    check_and_count(days_and_unit_dictionary)
