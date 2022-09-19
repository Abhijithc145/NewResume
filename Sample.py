thislist = "['English', 'Malayalam','jsdkj@gmai']"

# # print(list(value))
thislist=thislist.replace('"', ' ')
# thislist=thislist.replace("'", ' ')

# data = list(thislist.split(" "))

# print(list(thislist))
# print(type(data)) 



import ast
# x = '[ "Adhfajks","Basd","C" , " D"]'
y= ast.literal_eval(thislist)
print(type(y))
print(y)
for i in y:
    print(i)

# # ['A', 'B', 'C', ' D'] 
# y = [n.strip() for n in thislist] 
# print(y,"llllllllllllllllllllllll")
# # ['A', 'B', 'C', 'D']