import sys, array as arr; 

student_role_no = arr.array("i" ,[10,2,44,21,25,90,59,6,77,85]); 
result_found = -1;

try: 
    search_val = int(sys.argv[1]); 
except IndexError:
    print("Please enter search key"); 
    exit(1); 

try: 
    for i,v in enumerate(student_role_no): 
        if v == search_val:
            result_found = i;
            break;
    
except: 
    print("Something went wrong!"); 
    exit(1);

if result_found > -1: 
    print("Search result %d found at position %d" %(search_val, i))
else: 
    print("No result found!")