# 1) Create a list with a few fruit names:
#    a) Store multiple string items inside a list variable.
fruits=["banana", "apple", "orange", "mango"]

# 2) Print basic list details:
#    a) Print the length of the list using `len()`.
#    b) Print the first element using index `[0]`.
#    c) Print the last element using index `[-1]`.
print(len(fruits))
print(fruits[0])
print(fruits[-1])
# 3) Add a new item to the list:
#    a) Use `.append()` to add one more fruit.
#    b) Print the updated list.
fruits.append("grapes")
print(fruits)

# 4) Remove an item from the list:
#    a) Use `.remove()` to delete a specific fruit by name.
#    b) Print the updated list.
fruits.remove("apple")
print(fruits)
# 5) Sort the list:
#    a) Use `.sort()` to arrange items in alphabetical order.
#    b) Print the sorted list.
fruits.sort()
print(fruits)
# 6) Remove an item using index:
#    a) Use `.pop(index)` to remove an element at a specific position.
#    b) Print the updated list.
fruits.pop(3)
print(fruits)
# 7) Reverse the list order:
#    a) Use `.reverse()` to reverse the items.
#    b) Print the reversed list.
fruits.reverse()
print(fruits)
# 8) Multiply the list:
#    a) Print the list repeated multiple times using `list * 2`.
print(fruits*2)

# 9) Slice the list:
#    a) Keep only the first few elements using slicing (example: `list[:4]`).
#    b) Print the sliced list.
fruits[:4]
print (fruits)
# 10) Clear the list:
#     a) Use `.clear()` to remove all elements.
#     b) Print the updated (empty) list.
fruits.clear()
print(fruits)