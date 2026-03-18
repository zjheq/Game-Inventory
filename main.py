

inventory =  {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, "potion": 10}


def display(stuff):
    
    print("Inventory: ")
    total = 0
    for k, v in stuff.items():
        print(f"{v} {k}")
        total += v 
        
    print(f"total items: {total}")

def addItem(inv, loot):
    
    for i in loot: 
        if i in inv:
            inv[i]+=1
        
        else:
            inv[i] = 1


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    
    
while True:
    print("""
\nDecide your action:

1: Show inventory
2: Get dragon Loot
3: Exit                         
          """
          )
    try:
        user = int(input("> ").strip())
    
    except ValueError:
          print("Numbers only!")
          continue
    
    if user == 1:  
        display(inventory)
    
    elif user == 2:
        addItem(inventory, dragonLoot)
    
    elif user == 3:
        break
    
    else:
        print("1-3 only!")