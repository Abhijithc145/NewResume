# thislist = "['English', 'Malayalam','jsdkj@gmai']"

# # # print(list(value))
# thislist=thislist.replace('"', ' ')
# # thislist=thislist.replace("'", ' ')

# # data = list(thislist.split(" "))

# # print(list(thislist))
# # print(type(data)) 



# import ast
# # x = '[ "Adhfajks","Basd","C" , " D"]'
# y= ast.literal_eval(thislist)
# print(type(y))
# print(y)
# for i in y:
#     print(i)

# # # ['A', 'B', 'C', ' D'] 
# # y = [n.strip() for n in thislist] 
# # print(y,"llllllllllllllllllllllll")
# # # ['A', 'B', 'C', 'D']




# import json
  
# filename = 's.pdf'
# print(filename)
 
# dict1 = {}
  
# data1= open(filename) 
# print(data1)
# for line in data1:
#     command, description = line.strip().split(None, 1)
#     dict1[command] = description.strip()

# # creating json file
# # the JSON file is named as test1
# out_file = open("test5.json", "w")
# print(json.dump(dict1, out_file, indent = 4, sort_keys = False))
# out_file.close()


import json
import pdf_to_json as p2j

# web document : UDHR
url = "https://www.ohchr.org/EN/UDHR/Documents/UDHR_Translations/eng.pdf"

# Convert the document into a python dictionary
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lDict = lConverter.convert(url)

print(json.dumps(lDict, indent=4))