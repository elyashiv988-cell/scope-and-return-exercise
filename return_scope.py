# 1 the function printed 8 and the value score out of the function printed 10. 
# 2 the function printed Spy (name), 40 (level), and out the function printed agent(name), 2(level). 
# 3 the function printed 30 ((5+10)*2), the volue coins printed 20. 
# 4 the function printed 70 (100-30), 35(30+5). out of function the value health printed 100. 
# 5 both printed ['map', 'key', 'torch', 'coin'] because when the function called <items> (list) it isn't copy the varible but just points the index of items in the memory so when we change items the memory has changed. 
# 6 
items = ["map", "key"]

def replace_items():
    items = ["potion"]
    items.append("shield")
    print(items)

replace_items()
print(items)
