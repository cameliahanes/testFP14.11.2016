'''
Created on 14 nov. 2016

@author: Camelia
'''
def addInList(phones, phone):
    """function to add a new phone to the existing list"""
    phones.append(phone)
    

def add_(phones, man, model, price):
    p = {"manufacturer":man, "model":model, "price":price}
    phones.append(p)
    
    
def findPhoneMan(phones, manufacturer):
    """function to return the list of phones from a certain manufacturer
    parameters:
     the list of phones
     the manufacturer who makes the phones
    output : the list required
    """
    p = []
    for i in range(0, len(phones)):
        #if phones["manufacturer"] == manufacturer:
        if phones[i].get("manufacturer") == manufacturer:
            man = manufacturer
            model = phones[i].get("model")
            price = phones[i].get("price")
            add_(p, man, model, price)
            #printPhone(ph)
    return p

def printPhone(p):
    """returns a string with the phone's characteristics"""
    
    s = ""
    s += "Manufacturer: "+ str(p.get("manufacturer"))+", "+ "model: "+str(p.get("model"))+", "+ "price: "+ str(p.get("price")) + "\n"
    return s
    


def printList(phones):
    """prints the list of all phnes from the list given as input"""
    for phone in phones:
        #print(printPhone(phone))
        print(printPhone(phone))
        print("\n")



def addPhoneMenu(phones):
    """menu for adding a new phone
    raises value error if the values do not match te required types
    """
    try:
        man = input("Enter the manufacturer of the phone: ")
        model = input("Enter the model of the phone: ")
        price = input("Enter the price of the phone: ")
        
        if len(man) < 3 or len(model) < 3 or int(price) < 100:
            print("One of the fields doesn't match, can't add phone.")
            return
        else:
            phone = {"manufacturer":man, "model":model, "price":price}
            return deepcopy(add_(phones, man, model, price))
    except ValueError:
        print("Input doesn't match the required values.")

def findPhone(p, man, model):
    """"returns the index of the phone found in list, -1 instead
    params : the manufacturer and the model
    """
    for i in range(0, len(p)):
        if p[i].get("manufacturer") == man and p[i].get("model") == model:
            return i
    return -1

             
def changePriceMenu(phones):
    """menu for changind the prices of all phones"""
    try:
        man = input("Enter the manufacturer: ")
        model = input("Enter model: ")
        a = int(input("Enter the amount: "))
        if findPhone(phones, man, model) == -1:
            print("Phone not found.")
            return
        else:
            if a < -50 or a > 100:
                print("Invalid amount.")
                return
            i = findPhone(phones, man, model)
            am = int( a * phones[i]["price"]) / 100 
            phones[i]["price"] = deepcopy(int(phones[i]["price"]) + am)
            return deepcopy(phones)
    except ValueError:
        print("Invalid input")


def increasePricePhone(phone, amount):
    am = int(phone.get("price"))*int(amount)/100
    phone["price"] = int(phone.get("price")) + am
    return deepcopy(phone)
    
from copy import deepcopy
def increasePricesMenu(p):
    try:
        am = int(input("Enter the amount: "))
        if am < -50 or am > 100:
            print("Invalid amount.")
            return
        for i in range(0, len(p)):
            p[i] = deepcopy(increasePricePhone(p[i], am))
            return deepcopy(p)
    except ValueError:
        print("Invalid amount.")
