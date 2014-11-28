
#INPUT FUNCTIONS

def input_currency():
    print("Please enter the currency you wish to convert by entering the corresponding number: ")
    print("1. British Pound Sterling")
    print("2. Euro")
    print("3. U.S Dollar")
    input_currency = int(input(""))
    return input_currency

def output_currency():
    print("Please enter the currency you wish to convert to by entering the corresponding number: ")
    print("1. British Pound Sterling")
    print("2. Euro")
    print("3. U.S Dollar")
    output_currency = int(input(""))
    return output_currency

def input_amount():
    input_amount = float(input("Please enter the amount you wish to convert: "))
    return amount

#SORTING FUNCTION

def converter(input_currency, output_currency, input_amount):
    if output_currency == 1:
        pound_converter(input_amount, input_currency)
    elif output_currency == 2:
        euro_converter(input_amount, input_currency)
    elif output_currency == 3:
        usd_converter(input_amount, input_currency)
    else:
        print("Invalid")

##POUND FUNCTIONS
        
def pound_converter(amount, input_currency):
    if input_currency == 2:
        euro_gbp(amount)
    elif input_currency == 3:
        usd_gbp(amount)
    else:
        print("Invalid")

def euro_gbp(amount):
    total_amount = amount * 0.814
    return total_amount

def usd_gbp(amount):
    total_amount = amount * 0.625
    return total_amount


##EURO FUNCTIONS

def euro_converter(amount, input_currency):
    if input_currency == 1:
        gbp_euro(amount)
    elif unput_currency == 3:
        usd_euro(amount)
    else:
        print("Invalid")

def gbp_euro(amount):
    total_amount = amount * 1.229
    return total_amount

def usd_euro(amount):
    total_amount = amount * 1.601
    return total_amount


##USD FUNCTIONS

def usd_converter(input_currency, amount):
    if input_currency == 1:
        gdp_usd(amount)
    elif input_currency == 2:
        euro_usd(amount)
    else:
        print("Invalid")

def gdp_usd(amount):
    total_amount = amount * 0.625
    return total_amount

def euro_usd(amount):
    total_amount = amount * 1.302
    return total_amount

#DISPLAY FUNCTION

def display_total(input_currency, amount, output_currency, total_amount):
    print("You will have {0:.f} money".format(total_amount)


    



#MAIN PROGRAM
    
def currency_converter():
    input_currency = input_currency()
    amount = input_amount()
    output_currency = output_currency()

    total_amount = converter(input_currency, amount, output_currency)

    display_total(input_currency, amount, output_currency, total_currency)

currency_converter()
    
        


