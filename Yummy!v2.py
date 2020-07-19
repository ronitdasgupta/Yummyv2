"""
mealInfo = {}
Yes = ["Yes", "y", "yes", "Y", "yup", "Yup", "Yep", "yep", "yeah", "Yeah", "Yea", "yea", "Of course", "of course"]
No = ["No", "no", "Nope", "nope", "N", "n", "Nah", "nah", "na", "Na"]
moreMeal = ""
ingredientInfo = []
ingredientDict = {}

"""
"""
Dictionary Format:
mealInfo = {
    "Biryani": [{"Ingredient": "chicken", "Quantity": 2}, {"Ingredient": "rice", "Quantity": 2}],
    "Pasta": [{"Ingredient": "noodles", "Quantity": 4}, {"Ingredient": "sauce", "Quantity": 1}]
}
"""

"""
def fileWrite(dictionary):
    file = open("meals.txt", "w")
    for key, value in dictionary.items():
        file.write(key + (" : ") + "\n")
        for item in value:
            for key, value in dictionary.items():
                file.write(key + (" : ") + "\n")
                file.write(item)
            file.write(item + "\n")
        file.write("\n")
    file.close()
"""

def stripLastCharacters(answer, num):
    strip = answer[:-num]
    return strip

def fileWrite(dictionary):
    file = open("meals.txt", "w")
    for key, value in dictionary.items():
        #file.write("Meal" + (" : ") + "\n")
        file.write(key + "\n")
        for item in value:
            for key, value in item.items():
                file.write(key + (":") + value + "\n")
                #file.write(value + "\n")
            #file.write(value + "\n")
    file.close()

def readFile():
    file = open("meals.txt", "r")
    readMeals = file.readlines()
    lmealInfo = {}
    lingredientDict = {}
    ingredientDictList = []
    identifyKey = True
    for line in readMeals:
        if ":" in line:
            strippedValueCharacter = stripLastCharacters(line, 1)
            KeyVal= strippedValueCharacter.split(":")
            lingredientDict[KeyVal[0]] = KeyVal[1]  #{KeyVal[0]: KeyVal[1]}
            if KeyVal[0] == "Category":
                ingredientDictList.append(lingredientDict)
                lmealInfo[key] = ingredientDictList
                ingredientDictList = []
                lingredientDict={}
        else:
            strippedKeyCharacter = stripLastCharacters(line, 1)
            key = strippedKeyCharacter
    return lmealInfo

def userChoice():
    print("Choose what you would like to do:")
    print("=====================================================")
    print("=====================================================")
    print("                    1 Add")
    print("                    2 Delete")
    print("                    3 Shopping List")
    print("                    4 Quit")
    print("                    5 Meals")
    chooseOption = input("Which option would you like to choose? ")
    print("=====================================================")
    print("=====================================================")
    return chooseOption

def checkIfMealInDict(meal, mealInfo):
    try:
        if meal in mealInfo:
            return True
        else:
            return False
    except:
        return False

"""
def checkIfIngredientInDict(ingredient, mealInfo):
    if ingredient in mealInfo.get("Ingredient"):
        return True
    if ingredient not in mealInfo.get(mealAnswer, "Ingredient"):
        return False
"""

"""
def checkIfIngredientInList(ingredient, dictionary):
    if ingredient in dictionary.values:
        return True
    if ingredient not in dictionary.values:
        return False
"""

"""
def checkIfIngredientInList(ingredient, dictionary):
    for key, value in dictionary.items():
        if ingredient in value:
            return True
        if ingredient not in value:
            return False
"""

"""
def checkIfIngredientInList(ingredient, dictionary):
    try:
        if ingredient in dictionary:
            return True
        else:
            return False
    except:
        return False
"""

"""
def checkIfIngredientInList(ingredient, dictionary):
    try:
        if dictionary.get("Ingredient") == ingredient:
            return True
        else:
            return False
    except:
        return False
"""

"""
def checkIfIngredientInList(ingredient, dictionary):
    try:
        if ingredient in dictionary.get("Ingredient"):
            return True
        else:
            return False
    except:
        return False
"""


def checkIfIngredientInList(ingredient, list):
    try:
        for item in list:
            for item in list:
                findValue = item.get("Ingredient")
                if findValue == ingredient:
                    return True
                else:
                    continue
                    #return False
        return False
    except:
        return False


"""
def checkIfIngredientInList(ingredient, list, dictionary):
    for item in list:
        findValue = dictionary.get("Ingredient")
        if findValue == ingredient:
            return True
        else:
            return False
"""
def addMealInformation(mealInfo):
    moreMeal = ""
    mealAnswer = ""
    ingredientInfo = []
    ingredientDict = {}
    ingredientList = []
    Yes = ["Yes", "y", "yes", "Y", "yup", "Yup", "Yep", "yep", "yeah", "Yeah", "Yea", "yea", "Of course", "of course"]
    No = ["No", "no", "Nope", "nope", "N", "n", "Nah", "nah", "na", "Na"]
    while moreMeal not in No:
        #mealInfo = {}
        mealAnswer = input("Enter one meal please. ")
        mealInDict = checkIfMealInDict(mealAnswer, mealInfo)
        if mealInDict == True:
            print("Please enter a meal which you have not previously entered")
            continue
        if mealInDict == False:
            while moreMeal not in No:
                ingredientAnswer = input("What is an ingredient for" + " " + mealAnswer + "? " )
                #ingredientInDict = checkIfIngredientInList(ingredientAnswer, ingredientDict)
                ingredientInDict = checkIfIngredientInList(ingredientAnswer, ingredientInfo)
                if ingredientInDict == True:
                    print("Please enter an ingredient which you have not previously entered")
                    continue
                if ingredientInDict == False:
                    ingredientDict["Ingredient"] = ingredientAnswer
                    ingredientAmount = input("Quantity of" + " " + ingredientAnswer + " ? ")
                    ingredientDict["Quantity"] = ingredientAmount
                    ingredientCategoryAnswer = input("What category does" + " " + ingredientAnswer + " " "go in? ")
                    ingredientDict["Category"] = ingredientCategoryAnswer
                    ingredientInfo.append(ingredientDict)
                    moreIngredient = input("Would you like to add another ingredient? ")
                    if moreIngredient in Yes:
                        mealInfo[mealAnswer] = ingredientInfo
                        ingredientDict = {}
                        continue
                    if moreIngredient in No:
                        mealInfo[mealAnswer] = ingredientInfo
                        ingredientDict = {}
                        ingredientInfo = []
                        moreMeal = input("Would you like to add another meal? ")
                        if moreMeal in Yes:
                            break
                    while moreIngredient not in (Yes) and moreIngredient not in (No):
                        print("Please enter a valid response")
                        continue
    if moreMeal in No:
        fileWrite(mealInfo)
        return mealInfo
        print("Thank you for providing me the information!")
        #userChoice()
        #choice = userChoice()

def clearScreen():
    counter = 0
    while counter != 7:
        print("")
        counter += 1


#===========================================================
#PROGRAM STARTS HERE

#mealInfo = {}
#Yes = ["Yes", "y", "yes", "Y", "yup", "Yup", "Yep", "yep", "yeah", "Yeah", "Yea", "yea", "Of course", "of course"]
#No = ["No", "no", "Nope", "nope", "N", "n", "Nah", "nah", "na", "Na"]
#moreMeal = ""
#ingredientInfo = []
#ingredientDict = {}
#ingredientList = []

mealInfo = readFile()
#print(mealInfo)

addMeal = ""
deleteMeal = ""
moreChooseMeal = ""
#chooseOption = ""


while True:
    choice = userChoice()
    addIngredient = ""

    if choice == "2" or choice == "Delete" or choice == "delete":
        print("The meals you have entered are below:")
        for key, value in mealInfo.items():
            print(key)
        deleteChoose = input("Which meal would you like to delete? ")
        if deleteChoose in mealInfo:
            del mealInfo[deleteChoose]
            fileWrite(mealInfo)
            # userChoice()
            #choice = userChoice()
            clearScreen()
            continue

    if choice == "3" or choice == "Shopping List" or choice == "shopping list" or choice == "Shopping list" or choice == "shopping List":
        Yes = ["Yes", "y", "yes", "Y", "yup", "Yup", "Yep", "yep", "yeah", "Yeah", "Yea", "yea", "Of course",
               "of course"]
        No = ["No", "no", "Nope", "nope", "N", "n", "Nah", "nah", "na", "Na"]
        ingredientList = []
        while choice == "3" or choice == "Shopping List" or choice == "shopping list" or choice == "Shopping list" or choice == "shopping List":
            print("The meals you have entered are below:")
            for key, value in mealInfo.items():
                print(key)
                #print(key, sep = "", end = "", flush = True)
            chooseMeal = input("Choose a meal you would like to be in your ingredient list ")
            if chooseMeal in mealInfo:
                getMeals = mealInfo.get(chooseMeal)
                #addIngredient = getMeals
                ingredientList.append(getMeals)
                moreChooseMeal = input("Would you like to choose another meal to be in your ingredient list? ")
                if moreChooseMeal in Yes:
                    continue
                if moreChooseMeal in No:
                    print("Thank you! Your ingredient list is below:")
                    for ingredient in ingredientList:
                        print("==============================================")
                        for answer in ingredient:
                            for key, value in answer.items():
                                #print(key)
                                print(key + " : ", sep = " ", end = " ", flush = True)
                                print(value)
                                #print(value, sep = " ", end = " ", flush = True)
                    # userChoice()
                    #choice = userChoice()
                    clearScreen()
                    break
        continue

    if choice == "4" or choice == "Quit" or choice == "quit":
        exit()

    if choice == "5" or choice == "Meals" or choice == "meals":
        print("The meals you have entered is below:")
        for key, value in mealInfo.items():
            print(key)
        # userChoice()
        #choice = userChoice()
        clearScreen()
        continue

    if choice == "1" or choice == "Add" or choice == "add":
        #addMealInformation(mealInfo)
        mealInfo = addMealInformation(mealInfo)
        clearScreen()
        continue



# The variable chooseOption/choice does not change values


if choice == "1":
    while True:
        break











"""
if deleteMeal in No:
    while True:
        print("The meals you have entered are below:")
        for key, value in mealInfo.items():
            print(key)
        chooseMeal = input("Choose a meal you would like to add for your ingredient list ")
        if chooseMeal in mealInfo:
            getMeals = mealInfo.get(chooseMeal)
            ingredientList.append(getMeals)
            moreChooseMeal = input("Would you like to choose another meal to add to your ingredient list? ")
            if moreChooseMeal in Yes:
                continue
            if moreChooseMeal in No:
                print("Thank you! Your ingredient list is below:")
                for ingredient in ingredientList:
                    print(ingredient)
                break

if moreChooseMeal in No:
    exit()
"""


