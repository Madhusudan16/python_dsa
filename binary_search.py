import sys, numpy as np, time; 



student_number = np.array(range(1000000000));

scanned_rec = 0; 
start_time = time.time()
def binary_search(students, search_val) :
    global scanned_rec
    no_of_ele = len(students);
    mid_ele_index = int(no_of_ele * 50 / 100)
    
    new_student_arr = np.array_split(students, 2)
    
    for tmp_arr in new_student_arr:
        if tmp_arr[mid_ele_index - 1 ] >=  search_val:
             if len(tmp_arr) > 50:
                 return binary_search(tmp_arr, search_val)
             else: 
                for index, val in enumerate(tmp_arr): 
                    if val == search_val: 
                        scanned_rec = scanned_rec + 1 
                        return scanned_rec;
                    else: 
                        scanned_rec = scanned_rec + 1 
        else: 
            scanned_rec  = scanned_rec +  len(tmp_arr)
            
    return -1
        
def binary_search_1(list1, find): 
    low = 0
    high = len(list1) - 1 
    mid = 0
    while low <= high:
        mid = (high+low)//2
        if list1[mid] < find:
            low = mid + 1
        elif list1[mid] > find:
            high = mid - 1
        else:
            return mid
    return -1


try: 
    search_no = int(sys.argv[1])
except IndexError: 
    print("Invalid parameter");


result= binary_search_1(student_number, search_no); 

if result == -1:
    print("No such result found!"); 
else: 
    print("Search result %d found at %d position" %(search_no,result -1))

end_time = time.time()
execution_time = end_time - start_time
print("Script execution time:", execution_time, "seconds")
