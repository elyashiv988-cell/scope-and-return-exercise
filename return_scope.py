# 1 the function printed 8 and the value score out of the function printed 10. 
# 2 the function printed Spy (name), 40 (level), and out the function printed agent(name), 2(level). 
# 3 the function printed 30 ((5+10)*2), the volue coins printed 20. 
# 4 the function printed 70 (100-30), 35(30+5). out of function the value health printed 100. 
# 5 both printed ['map', 'key', 'torch', 'coin'] because when the function called <items> (list) it isn't copy the variable but just points to the same object in memory so when we change items the memory has changed. 
# 6 the function printed ["potion","shield"] because we create a new variable items in the function but the global items doesn't change. so the global items printed ["map", "key"]
# 7 both printed 20 because the keyword 'global' overwrite the global value point
# 8 the function runs form inside to outside and the value status run only in the score,so firest def inner printed running, secend def outer printed ready, therd the global value status printed waiting. 
# 9 def inner takes and overwrite the coins from def outer (by 'non local' keyword). so def inner and def outer printed 16, but the global coins doesn't chande so it prints 10. 
# 10 firet of all, all bag printed ['key', 'map', 'coin'] because when we add values to bag it changes the global bag because it's list so the variable just passed by refernce. the variable score in def inner takes and overwrite score from def outer (by 'non local' keyword) so in def outer score=10 , score=score*2 (total 20) then we call the def inner: score=score+5 so in the inner score=25. then we call the outer who overwrite by inner so score = 25 also. but the global score hasn't changed so score=1. 

#======
#part 2

# 1 mission distance

def convret_to_cm(meters):
    return meters*100
def print_distance(cm):
    return (f"robot moved {cm} centimeters")

dis_in_sm=convret_to_cm(1)
messege=print_distance(dis_in_sm)

# 2 simple price calculator

def adding_delivery_price(price):
    return price+10
def multyply_price(new_price):
    return new_price*2

price_with_delivery=adding_delivery_price(50)
final_price=multyply_price(price_with_delivery)
print(final_price)

# 3 name formatter

def print_name(first_name,last_neme):
    return first_name,last_neme
   
def print_upper_name(full_name):
    full_name_upper=[]
    for i in full_name:
        full_name_upper.append(i.upper())
    return full_name_upper

full_name=print_name("eli","cohen")
upper_name=print_upper_name(full_name)
print(upper_name)
            
# 4 temperature report

def convert_temp(celsius):
    fahernheit=celsius *1.8 + 32
    return fahernheit
def print_result(temp):
    return ("the celsius temperature is:",temp)
fahernheit=convert_temp(29)
print(print_result(fahernheit))

# 5 game health valvulator

def take_damage(health,damage):
    return health-damage

def adding_healing(health,healing):
    return health+healing

health_after_dange=take_damage(100)
final_health=adding_healing(health_after_dange)
print(final_health)


# 6 shopping bag total

def sum_products(a,b,c):
    total=0
    total+=a
    total+=b
    total+=c
    return total
def discount_price(price):
    return total-(total/100*20)

total=sum_products(20,50,100)
print(discount_price(total))



    



