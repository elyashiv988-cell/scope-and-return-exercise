# 1 the function printed 8 and the value score out of the function printed 10. 
# 2 the function printed Spy (name), 40 (level), and out the function printed agent(name), 2(level). 
# 3 the function printed 30 ((5+10)*2), the volue coins printed 20. 
# 4 the function printed 70 (100-30), 35(30+5). out of function the value health printed 100. 
# 5 both printed ['map', 'key', 'torch', 'coin'] because when the function called <items> (list) it isn't copy the varible but just points the index of items in the memory so when we change items the memory has changed. 
# 6 the function printed ["potion","shield"] because we create a new varible items in the function but the global doesn't change. so the glibal items printed ["map", "key"]
# 7 both printed 20 because the command 'global' overright the global value point
# 8 the function runs form inside to outside and the value status run only in the score,so firest def inner printed running, secend def outer printed ready, therd the global value status printed waiting. 
# 9 def inner takes and over right the coins from def outer (bt the commend 'non local'). so def inner and def outer printed 16, but the global coins doesn't chande so it prints 10. 
# 10 firet of all, all bag printed ['key', 'map', 'coin'] because when we add values to bag it changes the global bag because it's list so the varible just points by refus. the varible score in def inner takes and over right from def outer (by 'non local' commend) so in def outer score=10 , score=score*2 (total 20) then we call the fef inner: scroe=score+5 so in the inner score=25. then we call the outer who over right by inner so score = 25 also. but the global score hasn't changed so score=1. 

