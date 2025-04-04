"""
Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument)
 and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added,
return the reference to the head node.

Note: The  argument is null for an empty list.

Input Format

The first line contains T, the number of elements to insert.
Each of the next T lines contains an integer to insert at the end of the list.

Output Format

Return a reference to the head node of the linked list.
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    
    def insert(self,head,data):
        new_node = Node(data)
        if head is None:
            return new_node
        
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        
        return head
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);