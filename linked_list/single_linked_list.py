class Node: 
    def __init__(self, data): 
        self.data = data;
        self.next = None;


class LinkedList: 
    def __init__(self):
        self.head = None; 
        
    # Add new Item in the list #
    def add(self,val): 
        node = Node(val);
        if(self.head == None): 
            self.head = node;
            return; 
        
        start_node = self.head; 
        while start_node != None: 
            if(start_node.next == None): 
                start_node.next = node; 
                break; 
            start_node = start_node.next; 
        return;
    # traversing  #
    def print_data(self): 
        start_node = self.head; 
        while start_node != None: 
            print (start_node.data, end=" -> "); 
            start_node = start_node.next;
        print(" null ");
    #search #
    def search(self, s): 
        node = self.head; 
        while node != None: 
            if(node.data == s):
                return True; 
            node = node.next; 
        return False;
    # delete #
    def delete(self, v): 
        node = self.head; 
        prev_node = None;
        while node != None: 
            if node.data == v: 
                if(prev_node == None) : 
                    self.head = node.next;
                else:
                    prev_node.next  = node.next; 
                del node; 
                return True;
            prev_node = node; 
            node = node.next;
        return False;
            


linked = LinkedList(); 
linked.add(5); 
linked.add(9); 
linked.add("Madhusudan"); 
linked.add(99); 

linked.print_data();

if linked.search("Madhusudan"): 
    print("value is found"); 
else: 
    print("No such value ");


if linked.delete(90): 
    print("data is deleted"); 
else: 
    print("Unable to delete selected val"); 
    
linked.print_data();
            