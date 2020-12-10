import random as random  # The Random package is imported to use the randint() function to get random values
import time  # time package is imported to get the use of time() function from it
from threading import Timer  # Timer package is imported to do threading
# in order to repeat the desired function until the program is closed


def sugarLevelTest():  # SugarLevelTest is a self Defined function
    # which is holding the if conditions to test the Sugar level and react as needed
    timing = time.time()  # Making the object of time as Time
    ConvertedTime = time.ctime(timing)  # Converting Time into ctime in order to get a Desired time and date patren
    file = open('Log.docs', 'a')  # Defining a normal text file named file to keep the logged records
    try:  # Using try block to catch any uncertainity in its except block
        for i in range(1, 8):  # Using a for loop to repeat the below codes
            randomValue = random.randint(0, 5)  # Generating Random int values from 0 to 5

            if 0 <= randomValue <= 1:  # Checking the if an elif and recording the logs in a doc file named file
                print("WORNING...!\nYour Sugar Level is too low, please take some sweet to normalized your Sugar Level ")
                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                file.write("You had a Low Sugar Level \n your current Sugar Level was: ")
                file.write(str(randomValue))
                file.write("\n")
                file.write(ConvertedTime)
                file.write("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                break
            elif randomValue == 2:
                print("It seems good, You have a normal Sugar Level")
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                file.write("You had a normal Sugar Level of: ")
                file.write(str(randomValue))
                file.write("\n")
                file.write(ConvertedTime)
                file.write("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                break
            elif 3 <= randomValue <= 5:
                print("Caution..!\n Your Sugar Level is currently High, Injecting Insulin")
                print("\n Present Sugar Level: ", randomValue)
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                file.write("You had a high Sugar Level\n Your Sugar Level was: ")
                file.write(str(randomValue))

                if randomValue == 5:  # using inner if and elif conditions to inject the required amount of insulin
                    # and record the logs
                    file.write("\nInjected 3mg Insulin \n Now you have a Normal Sugar Level of: ")
                    sugarLevel = (randomValue-3)
                    file.write(str(sugarLevel))
                    file.write("\n")
                    file.write(ConvertedTime)
                    file.write("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                    break
                elif randomValue == 4:
                    file.write("\nInjected 2mg Insulin \n Now you have a Normal Sugar Level of: ")
                    sugarLevel = (randomValue - 2)
                    file.write(str(sugarLevel))
                    file.write("\n")
                    file.write(ConvertedTime)
                    file.write("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                    break
                elif randomValue == 3:
                    file.write("\nInjected 1mg Insulin \n Now you have a Normal Sugar Level of: ")
                    sugarLevel = (randomValue - 1)
                    file.write(str(sugarLevel))
                    file.write("\n")
                    file.write(ConvertedTime)
                    file.write("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                    break
                file.write("\n")
                file.write(ConvertedTime)
                file.write("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                break

    except:   # the except block of try to catch any exception
        print("Oops...! something went wrong, check your code")
        file.close()


def Threading():  # Second function which is holding  the threading control
    sugarLevelTest()  # The first Function is being called in Second function to apply threading on it
    print("Loading the Sugar Level.....")

    Timer(5, Threading).start()


Threading()  # Calling the second Function to Run the program.
