my_list, lowest_val = [7, 12, 9, 4, 11], None
for val in my_list: 
    if(lowest_val == None or lowest_val > val): 
        lowest_val = val;
print("Lower value if %d" %lowest_val);