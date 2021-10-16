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
    
    def insertAtPosition(self,data,position):
        np=Node(data)
        temp=self.head
        for i in range(position-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np

    def insertAtEnd(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    
    def deleteAtBeginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    
    def deleteAtPosition(self,position):
        temp=self.head.next
        prev=self.head
        for i in range(position-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    
    def deleteAtEnd(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

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
L.display`()
L.insertAtBeginning(0)
L.display()
L.insertAtEnd(30)
L.display()
L.insertAtPosition(25,3)
L.display()
L.deleteAtBeginning()
L.display()
L.deleteAtEnd()
L.display()
L.deleteAtPosition(1)
L.display()