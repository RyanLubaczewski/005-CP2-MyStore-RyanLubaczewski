welcomeStatement = input(
    "Welcome to Matthew Mart. Are you an admin or a customer? ")
inventory = {}
inventory = {"Shirts": 200, "Hats": 420, "Shorts": 690}
menu = {}
menu = {"Shirts": 20, "Hats": 10, "Shorts": 15}
running = True
amount = 1
while running == True:

    if welcomeStatement == "c":
        print(menu)
        cart = input(
            "Here is what we offer at Matthew Mart. What would you like to purchase? "
        )
        bag = int(menu.get(cart))
        count = int(input("How much of it would you like to buy? "))
        amount = amount + (bag * count)

        print("Your total is")
        print(amount)
        more = input("Would you like to buy anything else?")

        if more == "y":
            print(menu)
        cart = input(
            "Here is what we offer at Matthew Mart. What would you like to purchase? "
        )
        bag = int(menu.get(cart))
        count = int(input("How much of it would you like to buy? "))
        amount = amount * bag * count

        print("Your total is")
        print(amount)
        more = input("Would you like to buy anything else? ")

        if more == "n":
            print("Thank you for shopping at Matthew Mart")
            

  
  
  
  

    if welcomeStatement == "a":
      print(inventory)
      adminAction = input( "here is the most recent inventory recording,would you like to change someting? ")

    if adminAction == "n":
        print("Thank you for working towards a better Matthew Mart")
        running = False


    if adminAction == "y":
      adminChoice=input("What do you wan't to do? ")
      if adminChoice == "u":
        change = input(
            "would you like to add or subtract form the inventory? ")

        if change == "s":

            subItem = input(
                "What is the name of the item you wan't to remove? ")
            sub = int(input("How much do you want to get rid of? "))
            newValue = int(inventory.get(subItem))
            finalValue = newValue - sub
            inventory.update({subItem: finalValue})
            print(inventory)

        if change == "a":
            subItem = input(
                "What is the name of the item you wan't to add to? ")
            add = int(input("How much do you want to add? "))
            newValue = int(inventory.get(subItem))
            finalValue = newValue + add
            inventory.update({subItem: finalValue})
            print(inventory)
            
      if adminChoice == "i":
        newItem = input("What is the name of the new item you wan't to add? ")
      add = int(input("How much do you want to add?  "))
      price = int(input("What do you wan't the price of the new item to be?"))
    
      inventory.append(newItem,add)









            