import datetime
# Name : Panjamapon Karnasuta Student ID : 61070367
def main():
    today = datetime.datetime.now()
    print("\nDate & Time")
    print("_______________\n")
    print("Year : ", today.strftime('%Y'))
    print("Days : ", today.strftime('%A' + " " + today.strftime('%d')))
    print("Month : ", today.strftime('%B\n'))
main()