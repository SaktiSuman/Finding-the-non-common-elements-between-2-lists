def diff(list1, list2):
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))
list1 = [12, 23, 44, 56, 67]
list2 = [12, 23, 56, 43, 34, 99]
diff(list1, list2)