# 005-CP2-MyStore
1.	Create an item:quantity dictionary, called `inventory`
2.	Create an item:cost dictionary, called `menu`.  Items should match those in the `inventory`.
3.  Ask user if they want to see (A)dmin options, or (C)ustomer options.  
4.	Admin options should include: 
- current inventory
- add a new item to the inventory
- increase or decrease a quantity
5. Customer options should show the menu, add items to a shopping cart, and display the total of the cart.
6.	Use appropriate functions

---

Notes on dictionary
menu = {}

menu = {"apple": 1.90,
"bannana": 2.50,
"pineapple": 5}

menu.update({"apple" : 1.3})
print(menu)

menu.update({"pear": 10})
print(menu)

menu["apple"] = 3.6
print(menu)
print()
print(menu["apple"])

def addValue(k, v=10):
menu.update({k : v})
print(menu)

addValue("strawberry",25)

other methods:
menu.clear()
menu.copy()
menu.fromKeys() #returns a dict with the specified k:v pair
menu.get('someKey') #returns the value
menu.items() #returns a list containing tuples
menu.keys() #returns a list containing the keys
menu.values() #returns the values
menu.pop('someKey') #removed the element
menu.popitem() #removes the last inserted k:v
menu.update('k':v) #updated the dict with the k:v
menu.setdefault() #returns the value of the specified key. If key does not exist: insert the k:v