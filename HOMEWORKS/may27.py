fav_food= ["maggi", "pasta", "burger", "pizza"]
print(len(fav_food))
print(fav_food[0])
print(fav_food[-1])
print(fav_food[:3])
fav_food.append("chocolate")
fav_food.remove("maggi")
fav_food.sort()
print(fav_food)
fav_food.reverse()
print(fav_food)
 
me={
    "name":"aryan"
    ,"age": 13, 
    "grade": 8
}
print(me["name"])
me["location"]="banglore"
me["siblings"]=1
print(me)
me.pop("grade")
print(me)

fav_numbers=[1,2,3,4]
fav_things=dict(zip(fav_numbers, fav_food))
print(fav_things)