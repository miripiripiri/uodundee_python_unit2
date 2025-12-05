    # Takes variables x, y, z. Compares them and if three conditions are met prints 'x, y, z!'

def checkVariables (x, y, z):

    if x < z and y > z + 4:

        if y > x + z:
            print("x, y, z!")


# Takes in a list and a string. If the string is longer than 5 characters it is added to the list.
# If the string is exactly 3 characters the last item in the list is removed.

def amendList (myList, myWord):

    if len(myWord) >= 5:
        myList.append(myWord)

    elif len(myWord) == 3:
        myList.pop()


# Checks if number1 < number2. If so, add 1 to number1 each iteration until it equals number2.
# Must print number1 before the while loop otherwise counting will start at number1 + 1.

def countFromTo (number1, number2):
    if number1 < number2:
        print(number1)
        while number1 < number2:
            number1 += 1
            print(number1)


# A 2D list containing 6 people with three pieces of information each; name, height and age.

listOfPeople = [["Name", "Height", "Age"],
                ["Edith", 150, 16,],
                ["Paolo", 168, 21,],
                ["Forrest", 186, 34,],
                ["Ruth", 147, 85,],
                ["Leo", 173, 24]]


# Checks the height of each person in listOfPeople and prints those taller than 160.

for i in listOfPeople:

    if i[1] == "Height":
        continue

    if i[1] >= 160:
        print(i[0])


# Checks the age pf each person in listOfPeople and prints those older than 25.

for i in listOfPeople:

    if i[2] == "Age":
        continue

    if i[2] >= 25:
        print(i[0])


# A list of numbers ascending from 0 to 10

ascendingNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Adds each number in the list to the previous number, except 0 which adds to itself

for i in ascendingNumbers:

    i = i + ascendingNumbers[i]
    print(i)


# Removes last item from ascendingNumbers until only 1 item remains.
# Prints the list at each iteration

while len(ascendingNumbers) > 1:

    ascendingNumbers.pop()
    print(ascendingNumbers)


# A list of numbers and a list of words

listOfNumbers = [12, 2, 5, 6, 7, 9, 3]
listOfWords = ["forget", "egg", "distance", "orange", "spider", "tree", "goat"]


# 2 integer variables

temperature = 20
myAge = 24


# Whilst the condition that my age is greater than the temperature is met,
# Each item from listOfNumbers and listOfWords are compared in order.
# If the number is larger than the length it is printed or vice versa, if they are the same 'Match!' is printed.

count = -1

for i in listOfNumbers:

    count += 1

    if i > len(listOfWords[count]):
        print(i)

    elif i < len(listOfWords[count]):
        print(listOfWords[count])

    else:
        print("Match!")


# 2D List of containing 6 cities with their current time and temperature

listOfCities = [["City", "Time", "Temperature"],
                ["London", 12, 25],
                ["Tokyo", 20, 27],
                ["Montreal", 7, 17],
                ["Sydney", 21, 13],
                ["Madrid", 13, 31],
                ["Doha", 14, 41]]


# Finds the hottest city from listOfCities

def findHottestCity ():

    for i in listOfCities:

        hottestCity = 0

        if i[2] == "Temperature":
            continue

        if i[2] > hottestCity:
            hottestCity = i

    print(hottestCity[0])

findHottestCity()
