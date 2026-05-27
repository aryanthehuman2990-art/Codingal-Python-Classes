students=[["aryan", 1],["baron",2],["caron",3],["darren",4],["earen", 5]]
def convert(name):
    dic1={}
    for i in students:
        dic1[i[0]]=i[1]
    return dic1
print(convert(students))
        

    
    