#Euan McElhoney
#14/11/2014
#Functions Starter - Task 4

basic_hours = float(input("Please enter the amount of basic hours you worked: "))
basic_rate = float(input("Please enter your basic pay rate: "))
overtime_hours = float(input(" Please enter the amount of overtime hours you worked: "))
overtime_rate = float(input(" Please enter your overtime rate: "))

basic_pay = basic_hours * basic_rate
overtime_pay = overtime_hours * overtime_rate
total_pay = basic_pay + overtime_pay

print("You have earned £{0}".format(total_pay))
