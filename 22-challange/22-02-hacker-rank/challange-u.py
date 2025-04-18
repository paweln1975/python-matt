class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        first = head
        while head:
            prev = head
            current = head.next
            while current:
                if current.data == head.data:
                    prev.next = current.next
                else:
                    prev = prev.next
                current = current.next
            head = head.next
        return first


mylist= Solution()

head=None
for i in range(3):
    head=mylist.insert(head, 5)
    head = mylist.insert(head, 6)
head=mylist.removeDuplicates(head)
mylist.display(head)