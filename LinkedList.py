class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  #insert Node at the end of linked List
  def insertNodeAtTail(self,new_node_data):
    new_node = Node(new_node_data)
    if self.head ==None:
      self.head = new_node
    else:
      self.tail.next= new_node
    self.tail =new_node

   #insert node At the head of linked list
  def insertNodeAtHead(self,new_node_data):
    new_node=Node(new_node_data)
    if self.head == Node:
      self.head =new_node
    else:
      new_node.next=self.head
      self.head=new_node
    return self.head
  
  #insert node at specific position
  def insertAtSpecificPosition(self,new_node_data,position):
    new_node=Node(new_node_data)
    temp=self.head
    if position==0:
      new_node.next=temp
      self.head=new_node
      return
    i=1
    while i!=position:
      temp=temp.next
      i+=1
    new_node.next=temp.next
    temp.next=new_node

  #print the element of linked list
  def printll(self):
    temp=self.head
    while temp != None:
      print(temp.data)
      temp=temp.next
 
  #Find the length of Linked List
  def countll(self):
    i=0
    temp=self.head
    while temp !=None:
      temp=temp.next
      i+=1
    return i
  
  #reverse the linked List
  def reversell(self):
    current=self.head
    prev=None
    while current!=None:
      next =current.next
      current.next =prev
      prev=current
      current=next
    self.head = prev
    return prev
  
  
  # delete node at particular position
  def deletell(self,position):
    temp=self.head
    if position ==0:
      self.head=temp.next
      return
    i =1
    while i!=position:
      temp=temp.next
      i+=1
    temp.next = temp.next.next
  
  #remove duplicate element from LinkedList
  def removeDuplicates(self):
    copy =self.head
    temp =self.head.next
    while copy.next!=None:
        if copy.data == temp.data:
            copy.next =temp.next
            temp=temp.next
        else:
            copy=copy.next
            temp=temp.next
    return self.head
 
 #Linear Search in linked list to search for a element in linked list
  def searchll(self,value):
    count =0
    temp =self.head
    while temp!=None:
      if temp.data == value:
        count=1
        break
      else:
        temp=temp.next
    if count ==1:
      print("Element Exist")
    else:
      print("Element Not Exist")

  #Bubble sort on Linked List
  def sort (self):
    if self.head !=None:
      i = self.head
      j =self.head.next
      while i!=None:
        j=i.next
        while j!=None:
          if i.data >j.data:
            temp =i.data
            i.data=j.data
            j.data=temp
          j=j.next
        i=i.next
   #check linked list is palindrome or not
  def isPalindrome():
    temp = self.head
    t1 =0
    t2=0
    n =1
    while temp != None:
        t1 = t1 + temp.data*n
        t2 =t2*10 +temp.data
        temp=temp.next
        n=n*10
    if t1 == t2:
        return 1
    else:
        return 0
    

if __name__ == "__main__":
  llist = LinkedList()
  n = int(input("Enter the no of element of linked list"))
  for i in range(0,n):
    elt = int(input())
    llist.insertNodeAtTail(elt)
  llist.insertNodeAtHead(int(input("Enter the element insert at head")))
  llist.countll()
  llist.reversell()
  llist.deletell(int(input("Enter the position of element u want to delete")))
  value,position = map(int,input("Enter the value and position where element to be insert").split())
  llist.insertAtSpecificPosition(value,position)
  llist.removeDuplicates()
  llist.searchll(int(input("Enter the value to be search")))
  llist.sort()
  llist.printll()
  print(isPalindrome)

  
