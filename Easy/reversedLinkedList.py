class Solution:
  def reversedLinkedList(self, head: ListNode):
    """

    what we are gonna do here, instead of reversing the actual value, we will be reversing the pointers.
    
    we will point the first pointer to None, since we know that by definition, the end of the linked list is pointing to None or null.
    
    this would go on until the last pointer for head is at None, that way, we know for sure that we have reached the end of the linked list and we have successfully reversed the pointers
    
    """
    previous_point = None
    # we initialize a None value, this is where we will be pointing the first element of the ListNode, it will become like this: Null <- 1
    while head:
      main_pointer = head
      # we store the original value to main_pointer so that we can go back to it for reference
      head = head.next
      # we move the original pointer to the next one, dont worry we still have access to the original since we initialized it at main_pointer
      main_pointer.next = previous_point
      #as mentioned earlier, point the list node back to None. it will become: None <- 1.
      previous_point = main_pointer
      #we never touched main_pointer yet so since we have pointed 1 to None, we now need to point, 2 to 1, in essence we're putting 1 to prev pointer and the rest continues.
    
    return previous_point

  # this returns the whole linked list where the pointers are now reversed.
  
  # dm me in anyway you can if you got lost along the way and I'll try to explain it to you, 1 on 1 with proper iterations on slide!
