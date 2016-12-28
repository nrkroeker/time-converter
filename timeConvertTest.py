# A program to receive an input of time in classic format and convert it to military format
print("1.3.9")

# Global variables
classicTime = ""
militaryTime = ""

def errorMessage():
    print("Incorrect format, try again.")
    main()

# Conversions
def convertTime():
    global classicTime, militaryTime
    timeParts = classicTime.split(":")
    newHour = ""
    # Check that time was inputted correctly
    if int(timeParts[0]) > 12 or int(timeParts[0]) < 0:
        errorMessage()
    elif int(timeParts[1]) >= 60 or int(timeParts[1]) < 0:
        errorMessage()
    elif int(timeParts[2]) >= 60 or int(timeParts[2]) < 0:
        errorMessage()
    else:
        # Checks to see if we are in the first or second half of the day
        if timeParts[3].lower() == "pm":
            newHour = int(timeParts[0]) + 12
            if newHour == 24:
                newHour = 0
                newHour = str(newHour)
        elif timeParts[3].lower() == "am":
            newHour = timeParts[0]
            newHour == str(newHour)
        else:
            errorMessage()

        militaryTime = str(newHour + ":" + timeParts[1] + ":" + timeParts[2])

# Set up the input, call functions, and print the result
def main():
    global classicTime, militaryTime
    classicTime = input("Input a time in HH:mm:ss:AM/PM format: ")
    convertTime()
    print("The time in military format is: " + militaryTime)

main()
