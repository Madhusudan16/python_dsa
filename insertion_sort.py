

def rsort(lst): 
    for i in range(1, len(lst)): 
        new_index = i 
        for j  in range(i - 1, -1, -1): 
            if lst[i] > lst[j]: 
                new_index = j
            
        if(new_index != i): 
            val = lst.pop(i)
            lst.insert(new_index, val)
        
    print(lst);

def sort(lst): 
    for i in range(1, len(lst)): 
        new_index = i
        for j in range(i - 1, -1 , -1): 
            if lst[i] < lst[j]:
                new_index = j
        if new_index != i:
            val = lst.pop(i)
            lst.insert(new_index, val)
    print(lst)

def sort_v2(lst): 
    for i in range(1, len(lst)): 
        new_index = i
        current_val = lst[i]
        for j in range(i - 1, -1, -1): 
            if(current_val < lst[j]): 
                lst[j + 1] =  lst[j]
                new_index = j
            else: 
                break

        if(new_index != i): 
            lst[new_index] = current_val
    print(lst)

list = [1,4,5,2,0];
sort_v2(list);

