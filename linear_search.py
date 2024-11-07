import sys, array as arr;

student_role_no = arr.array("i",[1,4,7,9,11,66,55,33,88,34,8]); 

try: 
    search_val = int(sys.argv[1]); 
except IndexError: 
    print("Please pass value to search in command line")
    exit(1);

try:
    result = student_role_no.index(search_val);
    print("Search Result %d found at %d index" %(search_val, result))
except ValueError as err:
    print(err)
    print("No result found");
