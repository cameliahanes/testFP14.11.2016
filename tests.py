'''
Created on 14 nov. 2016

@author: Camelia
'''
from operations import *


def testInitandAdd(p):
    p = []
    p1 = {"manufacturer":"Samsung", "model":"Note 5", "price":250}
    p.append(p1)
    p1 = {"manufacturer":"Samsung", "model":"Note 7", "price":850}
    p.append(p1)
    p1 = {"manufacturer":"Apple", "model":"Iphone5", "price":300}
    p.append(p1)
    p1 = {"manufacturer":"Apple", "model":"Iphone7", "price":700}
    p.append(p1)
    p1 = {"manufacturer":"Nokia", "model":"Lumia 400", "price":150}
    p.append(p1)
    p1 = {"manufacturer":"Nokia", "model":"Lumia 6", "price":290}
    p.append(p1)
    p1 = {"manufacturer":"Samsung", "model":"Note 2", "price":450}
    p.append(p1)
    p1 = {"manufacturer":"Samsung", "model":"Note 4", "price":280}
    p.append(p1)
    p1 = {"manufacturer":"Samsung", "model":"Notes", "price":950}
    p.append(p1)
    
    p1 = {"manufacturer":"Samsung", "model":"Note 0", "price":150}
    p.append(p1)
    #print(len(p), "\n")
    #addInList(p, phone)
    assert p[0]["manufacturer"] == "Samsung"
    assert p[0]["price"] == 250
    return p
            
def testInc():
    p = {"manufacturer":"Nokia", "model":"Lumia 400", "price":150}  
    p = increasePricePhone(p, 10)
    assert p.get("price") == 165          
    p = {"manufacturer":"Nokia", "model":"Lumia 400", "price":150}  
    p = increasePricePhone(p, -10)
    assert p.get("price") == 135

testInc()
  

