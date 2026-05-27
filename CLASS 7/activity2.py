# 1) Create dictionaries (empty, integer keys, mixed keys, simple details).
dic1={}
dic2={1:"pizza",2:"burger",3:"pasta"}
dic3={"name":"aryan", "age":13}
# 2) Access values:
#    a) Use `dict"[key]` and `dict.get(key)` to print values.
var=["name", "age"]
for i in var:
    print (f"{dic3.get(i)}")
var2=[1,2,3]
for i in var2:
    print (f"{dic2.get(i)}")

# 3) Update and add:
#    a) Update an existing key’s value.
#    b) Add a new key-value pair and print the dictionary.
dic2[2]="rice"
dic2[4]="burger"
print (dic2)

# 4) Remove and clear:
#    a) Remove a key using `.pop(key)` and print.
#    b) Access a value again using `.get()`.
#    c) Clear all items using `.clear()` and print the empty dictionary.
dic2.pop(1)
print (dic3.get("age"))
print (dic2)
print(dic3)
dic2.clear
dic3.clear
print(dic2)
print(dic3)