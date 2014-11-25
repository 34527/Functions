#Write a function that returns the total number of seconds, calculated from a whole number of hours,
#minutes and seconds provided as 3 parameters.Write a function that returns the total number of seconds,
#calculated from a whole number of hours, minutes and seconds provided as 3 parameters.

#Euan McElhoney
#21/11/2014
#development exercises 1

def input_time():
    hours = int(input("Please enter the total number of hours: "))
    minutes = int(input("Please enter the total number of minutes: "))
    seconds = int(input("Please enter the total number of seconds: "))
    return hours, minutes, seconds

def time_calculation(hours, minutes, seconds):
    total_seconds = (hours*60*60) + (minutes * 60) + seconds
    return total_seconds

def display(hours, minutes, seconds, total_seconds):
    print("{0} hours, {1} minutes, and {2} seconds is equivalent to {3} seconds".format(hours, minutes, seconds, total_seconds))

def main_program():
    hours, minutes, seconds = input_time()
    total_seconds = time_calculation(hours, minutes, seconds)
    display(hours, minutes, seconds, total_seconds)

main_program()
