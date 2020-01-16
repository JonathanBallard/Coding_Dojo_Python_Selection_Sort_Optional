

def Selection_Sort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - j - 1):
            if list[i+1] < list[i]:
                list[i+1], list[i] = list[i], list[i+1]
    return list

my_list = [1,3,65,73,21,589,54,2,155,60]

#print(Selection_Sort(my_list))




def Selection_Sort2(list):
    min = list[0]
    for j in range(len(list)):
        for i in range(j,len(list),1):
            if list[i] < list[j]:
                min = list[i]
                list[i] = list[j]
                list[j] = min
                
    return list




my_list2 = [11,3,65,73,21,589,54,2,155,60]

print(Selection_Sort2(my_list2))














