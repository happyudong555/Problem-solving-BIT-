import calendar
# Name : Panjamapon Karnasuta Student ID : 61070367
def main():
    # input to insert year and month
    year = int(input("Year : "))
    month = int(input("Month : "))

    print("_________________________\n")

    # receive year and month to render calendat table 
    print(calendar.month(year, month))
main()