a = [2,5,7,9,12,6,4,85,63,68,123,69,70]
# b = []
# for items in a:
#     if items%2 == 0:
#         b.append(items)
# print(b)

# shortcut to write above same code 
b = [i for i in a if i%2 == 0]
print(b)

#greater than 12 
# b = [i for i in a if i>12]
# print(b)

#set comprehension
t = (1,5,2,3,4,2,1,4)
s = {i for i in t}
print(s)
