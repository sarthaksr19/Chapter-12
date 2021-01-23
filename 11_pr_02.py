list1 = [5,6,3,8,9,4,12,13]
for index, items in enumerate(list1):
    if index == 0:
        continue
    elif index % 2 == 0:
        print(items)
    