'''
Created on 14 nov. 2016

@author: Camelia
'''
from tests import *
from operations import *
from copy import deepcopy
def mainn():
    m = ""
    m += "1 - Add a new phone; \n"
    m += "2 - Find phones from a certain manufacturer; \n"
    m += "3 - increase the price of a phone with a given amount; \n"
    m += "4 - increase the price of all phones with a given percent; \n"
    m += "x - exit; \n"
    print( m)

def main():
    commands = ["1", "2", "3", "4", "x"]
    phones = []
    
    phones = testInitandAdd(phones)
    while True:
        mainn()
        command = input("Enter the command: ")
        #printList(phones)
        if command in commands : 
            if command == "x":
                break
            elif command == "1":
                addPhoneMenu(phones)
            elif command == "2":
                man = input("Enter the manufacturer: ")
                if len(findPhoneMan(phones, man)) <= 0:
                    print("No phone to display.")
                else:
                    print(findPhoneMan(phones, man))
            elif command == "3":
                phones = deepcopy(changePriceMenu(phones))
            elif command == "4":                #print(phones)
                phones = deepcopy(increasePricesMenu(phones))
                print(phones)
        else:
            print("Invalid command.")


main()    