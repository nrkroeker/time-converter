# (A different version of) A program that converts an input of time in classic format into military format
# All input numbers must be zero-padded

classicTime = ""
militaryTime = ""

def errorMessage(errorType):
    print("Wrong %s formatting, try again.\n" % errorType)
    main()

def convertTime():
    global militaryTime
    # Set up local variables with slices of the input string
    hours = classicTime[0:2]
    minutes = classicTime[3:5]
    seconds = classicTime[6:8]
    middaySection = classicTime[8:10]
    newHours = 0

    # Check for correct formatting
    if int(hours) > 12 or int(hours) <= 0:
        errorMessage("hour")
    elif int(minutes) > 59 or int(minutes) < 0:
        errorMessage("minute")
    elif int(seconds) > 59 or int(seconds) < 0:
        errorMessage("second")
    else:
        # Check if it's AM or PM
        if middaySection.lower() == "pm":
            if int(hours) == 12:
                newHours = hours
            else:
                newHours = int(hours) + 12
        elif middaySection.lower() == "am":
            if int(hours) == 12:
                newHours = 0
            else:
                newHours = hours
        else:
            errorMessage("AM/PM")

        # Create time string
        militaryTime = (str(newHours) + ":" + minutes + ":" + seconds)

# Initiate all the things
def main():
    global classicTime, militaryTime

    classicTime = input("Enter time in format hh:mm:ssAM/PM: ")
    if classicTime == "08:12:43PM":
        print("The exact same as your sample input, hm? It works for other times too just FYI ;) \n")

    convertTime()

main()
print("The time in military format: " + militaryTime)