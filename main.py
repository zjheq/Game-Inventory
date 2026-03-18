

inventory =  {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, "potion": 10}


def display(stuff):
    
    print("Inventory: ")
    total = 0
    for i in stuff:
        print(f"{i}: {stuff[i]}")
        total += stuff[i] 
        
    print(f"total items: {total}")
    
display(inventory)