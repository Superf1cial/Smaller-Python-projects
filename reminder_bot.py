import time
import imaplib
import getpass

user = input("Enter your GMail username: ")
pwd = getpass.getpass("Enter your password: ")


print("Setting up reminder lists")

Thursday_List = ["Testvalue1","Testvalue2"]

print("Getting current date")
current_day = time.strftime("%A %d %m %Y")
current_day = current_day.split(" ")
print("Done, checking for reminder list")

def remind_you(selected_list):
    print("Logging into Google Mail - {}".format(time.strftime("%H:%M:%S")))
    m = imaplib.IMAP4_SSL("smtp.gmail.com")
    m.login(user,pwd)

if current_day[0] == "Monday":
    print("Reminding you for Monday Episodes")
    selected_list = Monday_List
    remind_you(selected_list)
elif current_day[0] == "Tuesday":
    print("Reminding you for Tuesday Episodes")
    selected_list = Tuesday_List
    remind_you(selected_list)
elif current_day[0] == "Wednesday":
    print("Reminding you for Wednesday Episodes")
    selected_list = Wednesday_List
    remind_you(selected_list)
elif current_day[0] == "Thursday":
    print("Reminding you for Thursday Episodes")
    selected_list = Thursday_List
    remind_you(selected_list)
elif current_day[0] == "Friday":
    print("Reminding you for Friday Episodes")
    selected_list = Friday_List
    remind_you(selected_list)
elif current_day[0] == "Saturday":
    print("Reminding you for Saturday Episodes")
    selected_list = Saturday_List
    remind_you(selected_list)
elif current_day[0] == "Sunday":
    print("Reminding you for Sunday Episodes")
    selected_list = Sunday_List
    remind_you(selected_list)
