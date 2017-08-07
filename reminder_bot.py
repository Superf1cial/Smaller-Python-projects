import time

Monday_Episodes = []
Tuesday_Episodes = []
Wednesday_Episodes = []
Thursday_Episodes = []
Friday_Episodes = []
Saturday_Episodes = []
Sunday_Episodes = []

def add_series(keyword):
    day, name = keyword.split(", ")
    print("Adding {} to {}list".format(name,day))
    if day == "Monday":
        Monday_Episodes.append(name)
        print(Monday_Episodes)
    elif day == "Tuesday":
        Tuesday_Episodes.append(name)
        print(Tuesday_Episodes)
    elif day == "Wednesday":
        Wednesday_Episodes.append(name)
        print(Wednesday_Episodes)
    elif day == "Thursday":
        Thursday_Episodes.append(name)
        print(Thursday_Episodes)
    elif day == "Friday":
        Friday_Episodes.append(name)
        print(Friday_Episodes)
    elif day == "Saturday":
        Saturday_Episodes.append(name)
        print(Saturday_Episodes)
    elif day == "Sunday":
        Sunday_Episodes.append(name)
        print(Sunday_Episodes)

def print_current_day():
    current_day = time.strftime("%a")
    if current_day == "Mon":
        print("Sending update for Monday")
    elif current_day == "Tue":
        print("Sending update for Tuesday")
    elif current_day == "Wed":
        print("Sending update for Wednesday")
    elif current_day == "Thu":
        print("Sending update for Thursday")
    elif current_day == "Fri":
        print("Sending update for Friday")
    elif current_day == "Sat":
        print("Sending update for Saturday")
    elif current_day == "Sun":
        print("Sending update for Sunday")


while True:
    print_current_day()
    keyword = input("Enter series name in format(Day, Name): ")
    add_series(keyword)
