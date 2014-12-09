#Euan McElhoney
#09/12/14
#Functions Spot Check - Q3

def journey_cost_calculator():
    distance, mpg, fuelprice = GetInput()
    total_cost_pound = CalculateCost(distance, mpg, fuelprice)
    DisplayCost(total_cost_pound)

    
def GetInput():
    distance = float(input("Please enter the distance in miles: "))
    mpg = float(input("Please enter the Miles per Gallon of the veichle: "))
    fuelprice = float(input("Please enter the cost of fuel per litre in pence: "))
    return distance, mpg, fuelprice

def CalculateCost(distance, mpg, fuelprice):
    gallon = distance / mpg
    total_litre = gallon * 4.55
    total_cost_pence = total_litre * fuelprice
    total_cost_pound = total_cost_pence / 100
    return total_cost_pound

def DisplayCost(total_cost_pound):
    print("The total of your journey is £{0:.2f}".format(total_cost_pound))
    
journey_cost_calculator()
