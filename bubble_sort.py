

list = [7, 3, 9, 12, 11];
def sort_desc(lst): 
    no_ele = len(lst) - 1
    for i in range(no_ele, 0, -1): 
        for j in range(i):
            print(lst)
            if lst[j] > lst[j+1]: 
                lst[j] = lst[j] + lst[j+1]
                lst[j+1] = lst[j] - lst[j+1]
                lst[j] = lst[j] - lst[j+1]

    print(lst);


def sort_asc(lst): 
    for i in range(len(lst) - 1): 
        is_sorted = True
        for j in range(len(lst) - 1 - i): 
            if lst[j] > lst[j + 1]: 
                lst[j], lst[j + 1] =  lst[j + 1], lst[j]
                is_sorted = False
        if(is_sorted): 
            break

#sort_desc(list);
sort_asc(list);
print(list)