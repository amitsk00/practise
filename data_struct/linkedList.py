import random 
from time import sleep 

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None 


class LinkedList():
    def __init__(self):
        self.head = None 
    
    ###########################################
    # Display LL
    def display_list(self):
        if not self.head:
            print(f"empty linked list")
        else: 
            curr_node = self.head 
            print(f"List is:")
            # sleep(5)

            while curr_node:
                print(curr_node.val , end=" > ")
                curr_node = curr_node.next
            
        print("\n\n  ")


    ###########################################
    # Add in LL    
    def add_node(self, val):
        new_node = Node(val) 

        if not self.head:
            # print("HEAD added")
            self.head = new_node
        else:
            curr_node = self.head 
            while curr_node.next:
                curr_node = curr_node.next 

            curr_node.next = new_node


    ###########################################
    # Search in LL
    def search_list(self, num : int) -> bool:         
        curr_node = self.head 
        found = False
        # print(f"looking for {num}")
        if not curr_node:
            print("EMty list, item not found")
        else:
            while curr_node:
                if curr_node.val == num:
                    found = True
                    break 
                curr_node = curr_node.next 
        
        return found 
        

    ###########################################
    # Delete from LL    
    def remove_node(self, num):
        curr_node = self.head
        tmp_node = curr_node
        while curr_node:
            if curr_node.val == num:
                print(f"about to delete {num}")
                
                if curr_node == self.head:
                    print("deleting HEAD")
                    self.head = tmp_node.next 
                else:
                    tmp_node.next = curr_node.next

                break 

            tmp_node = curr_node
            curr_node = curr_node.next 




if __name__ == "__main__":
    ll = LinkedList()


    # ###########################################
    # # specific test
    # for i in range(10):
    #     ll.add_node(i)
    # ll.remove_node(0)
    # ll.display_list()


    ###########################################
    # Add a number
    
    num1 = random.randint(1,100)
    for i in range(num1):
        ll.add_node(i)
    ll.display_list()    

    ###########################################
    # Search a number

    num1 = random.randint(1,99)
    found = ll.search_list(num1)
    if found:
        print(f"{num1} is found in Linked List")
    else:
        print(f"{num1} not found in Linked List")

    ###########################################
    # Delete a number
    
    num1 = random.randint(1,20)
    found = ll.search_list(num1)
    if found:
        ll.remove_node(num1)
    else:
        print(f"{num1} not found in LL")
    ll.display_list()


