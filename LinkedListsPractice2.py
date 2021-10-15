class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class SingleLinkedLists:
    def __init__(self):
        self.head=None
    
    def insertAtBeginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def insertAtEnd(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def display(self):
        if self.head is None:
            print("The list is empty")
        else:
            temp=self.head
            while temp:
                if temp.next is not None:
                    print(temp.data,"---->",end=" ")
                    temp=temp.next
                else:
                    print(temp.data)
                    temp=temp.next
L=SingleLinkedLists()
n1=Node(10)
L.head=n1
n2=Node(20)
L.head.next=n2
L.display()
L.insertAtBeginning(0)
L.display()
L.insertAtEnd(30)
L.display()