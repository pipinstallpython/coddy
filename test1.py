def merge_and_sort_descending(list1, list2):
    i, j = 0, 0
    merged_list = []

    while i < len(list1) and j < len(list1):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    if i < len(list1):
        merged_list += list1[i:]
    else: 
        merged_list += list1[j:]

    return merged_list


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = merge_and_sort_descending(list1, list2)
print(result)
