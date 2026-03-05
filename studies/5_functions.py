
def check_season(month):
    month = month.lower()

    if month == "december" or month == 'january' or month == 'february':
        return "Winter"

    if month == 'april' or month == 'march' or month == 'may':
        return "Spring"

    if month =='june' or month == 'july' or month == 'august':
        return "Summer"

    if month == 'september' or month == 'october' or month == 'november':
        return "Fall"
    
    else:
        print("Error!")

print(check_season("april"))