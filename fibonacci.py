import sys; 


def print_fibbo(till) :
    prev_num_first, prev_num_second = 0, 1;
    having_latest_val_in_sec = True
    print("%d \n%d " %(prev_num_first, prev_num_second ))
    for i in range(prev_num_second, till) : 
        if having_latest_val_in_sec:
            prev_num_first += prev_num_second
        else: 
            prev_num_second += prev_num_first
        print("%d" %(prev_num_first if having_latest_val_in_sec else  prev_num_second) )
        having_latest_val_in_sec = not having_latest_val_in_sec

print_fibbo(10)
