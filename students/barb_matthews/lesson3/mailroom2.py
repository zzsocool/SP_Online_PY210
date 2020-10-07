#! /usr/bin/env python3

## Lesson 3.3 Mailroom Part 1
## By: B. Matthews
## 9/28/2020
## This is the first of a four-part assignment that will keep track of an imaginary charity's
## donors, the donation amounts, and will print a thank you message if desired.

import sys
#import copy

index = []
person1 = ['Arthur Dent', [10.00, 10.00]]
person2 = ['Trillian Hmmm', [234.12, 1.00, 43.50]]
person3 = ['Zaphod B', [1000.00, 25.99, 321.45]]
person4 = ['James Maxwell', [1.00]]
person5 = ['Grace Hopper', [50.00, 300.00]]
person6 = ['Georg Ohm', [5500.50]]
person7 = ['Cynthia Irvine', [500.00, 20.00]]
average = 0

index = index + person1 + person2 + person3 + person4 + person5 + person6 + person7
#See what's in data structure
#print(index)

prompt = "\n".join(("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nMailroom for Lazy Fundraisers\n",
          "Please choose an option:",
          "1) Send a Thank-you",
          "2) Create a Report",
          "3) Quit",
          "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\a> "))

prompt2 = "\n".join(("**********************************\nThank-You Options\n",
          "What do you want to do?:",
          "name - Enter a name",
          "list - List of donor names",
          "   q - Quit",
          "**********************************\n> "))

def thanks(data):
    """Prints a donor thank-you to the screen, maybe user copies it to email"""
    #active_donor = []
    name = ''
    money = []

    while True:
        choice = input(prompt2)
        if choice.lower() == "name":
            found = 0
            name = input("What name?\n")

            ## check if name is in index, if not then add it
            for i, item in enumerate(data):
                if (not (i % 2)):           ## Compare the name fields
                    if (name == item):
                        found = i+1         ## points to donation amounts
                        print(item)
                    else:
                        data = data + name
                        found = len(data)
                        ## prompt for donation amount, add it to name record in the index
                        money = input("What donation amount?\n")
                        data = data + money
                        print("Added %s gave %f\n" % (name, money))

            ## use fstrings to display a thank-you letter to the screen

        elif choice.lower() == "list":
            print("The current names are: ")
            ## enumerate through the index and print names
            for i, item in enumerate(data):
                if (not (i % 2)):
                    print(item)
            print('\n')

        elif choice.lower() == "q":
            exit_menu()
        else:
            print("Try again.")
    return

def report():
    """Prints a report to the screen of donors and amounts"""

    return

def exit_menu():
    """Exits out of the interactive menu"""
    print("Ok, later")
    sys.exit()  # exit the interactive script

def main():
    """Prints the menu dispay to the screen and gets user input"""
    while True:
        response = input(prompt)  # continuously collect user selection
        if response == "1":
            thanks(index)
        elif response == "2":
            report()
        elif response == "3":
            exit_menu()
        else:
            print("\n" * 100)
            print("Try again. What option?")

# If not imported as a module, call the main function
if __name__ == "__main__":
    main()