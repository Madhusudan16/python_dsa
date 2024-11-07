def sort(list): 
    for i in range(len(list)): 
        min_val = min(list[i:])
        min_inx = list.index(min_val)
        list[min_inx], list[i] =  list[i], list[min_inx]
    


def sort_v2(lst): 
    for i in range(len(lst)) : 
        min_index = i
        for j in range(i + 1, len(lst)): 
            if lst[j] < lst[min_index]:
                min_index = j; 
        min_val = lst.pop(min_index); 
        lst.insert(i, min_val);
    print(lst);



list = [1,4,5,2,0];
sort_v2(list);
#print(list)