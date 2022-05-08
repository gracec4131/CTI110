def main():
    menu()

def menu():
    repeat = 1
    choice = 0
    scorelist = []
    while repeat != 0:
        print()
        print('----Menu----')
        print('1. Create Score List')
        print('2. Display Results')
        print('3. Exit')
        print('------------')


        choice = input("Enter a choice 1 or 2 or 3: ")
        if choice =="1":
               scorelist = listofscores()
        elif choice == '2':
             if len(scorelist) == 0:
                 print('List not created!')
             else:
                 calcscores(scorelist)
        elif choice == '3':
              repeat = 0
        else:
            print("Not a valid entry")
            print("Try again")
            repeat = 1
            print('Program terminated!')

def makelist(numscores):
    scores = []
    i = 0
    #Gets scores
    while i < numscores:
        score = int(input(f'Enter score #{i +1}: '))
        #Determines if score is less than zero or greater than 100
        if 0 > score or score > 100:
            print('Invalid Entry!\nEntry must be between 0 and 100!')
            i = i
        else:
            scores.appen(score)  #Adds each score to end of list
            i + i
