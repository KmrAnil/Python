class Node:
  def __init__ (self,data):
    self.data=data
    self.next=None
    self.pre=None
class DoubleLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  
  # insert node at the end of doubly linked list
  def insertAtTail(self,data):
    newNode = Node(data)
    if self.head == None:
      self.head = newNode
    else:
      newNode.pre=self.tail
      self.tail.next = newNode
    self.tail =newNode
  
  #insert a node at head
  def insertAtHead(self,data):
    newNode =Node(data)
    if self.head == None:
      self.head=newNode
    else:
      newNode.next =self.head
      self.head.pre=newNode
      self.head =newNode
  
  #insert node at any position
  def insertAtSpecificPosition(self,data,position):
    newNode = Node(data)
    temp = self.head
    if position == 0:
      newNode.next = self.head
      self.head=newNode
      return 
    else:
      i =0
      while i!= position-1:
        temp =temp.next
        i+=1
      if temp.next != None:
        newNode.next=temp.next
        temp.next.pre=newNode
        newNode.pre = temp
        temp.next =newNode
      else:
        newNode.pre =  temp
        temp.next = newNode
  
  # Delete doubly linked list in any position
  def deletedll(self,position):
    temp=self.head
    if position == 0:
      self.head=temp.next
      return
    i =1
    while i!=position:
      temp=temp.next
      i+=1
    if temp.next.next == None:
      temp.next=None  
    else:
      temp.next = temp.next.next
      temp.next.pre =temp

  #print the doubly linked list 
  def printdll(self):
    temp=self.head
    print("Print Linked list in forward Direction")
    while temp!=None:
      print(temp.data)
      temp=temp.next
  
  #print the doubly linked list in  backward Direction
  def printbackward(self):
    temp = self.tail
    print("Print linked List in backward direction")
    while(temp!=None):
      print(temp.data)
      temp =temp.pre


if __name__ =="__main__":
  dll=DoubleLinkedList()
  dll.insertAtTail(int(input("Enter the elt to be insert at end of ll :")))
  dll.insertAtTail(int(input("Enter the elt to be insert at end of ll :")))
  dll.insertAtTail(int(input("Enter the elt to be insert at end of ll :")))
  dll.insertAtTail(int(input("Enter the elt to be insert at end of ll :")))
  dll.insertAtHead(int(input("Enter the elt to be insert at start of ll :")))
  value,position = map(int,input("Enter the value and position where element to be insert").split())
  dll.insertAtSpecificPosition(value,position)
  dll.deletedll(int(input("Enter the position of element u want to delete")))
  dll.printdll()
  dll.printbackward()
