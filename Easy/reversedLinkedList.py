class Solution:
  def reversedLinkedList(self, head: ListNode):
    #so basically what we are gonna do here, instead of reversing the actual value, we will be reversing the pointers.
    #we will be having the first pointer to point to None, since we know that by definition, the end of the linked list is pointing to None or null.
    #this would go on until the last pointer for head is at None, that way, we know for sure that we have reached the end of the linked list and we have successfully reversed the pointers.
    previous_point = None
    # we set the previous point as none as we would be pointing the main pointer backwards.
    while head:
      main_pointer = head
      # we basically just put the original value first so that for every iteration, we will have a value for the current, the next pointer for main_pointer will be pointed to prev_point.
      head = head.next
      # this is basically moving the original pointer to the next one so that we can still access is even if we move the next value for main_pointer.
      main_pointer.next = previous_point
      #as mentioned earlier, point the list node back to None. it will become like 1 -> 0.
      previous_point = main_pointer
      #then we put the value of 1 to previous point since it was the previous point after we point the mainpointer to next.
    
    return previous_point
  # this returns the whole linked list where the pointers are now reversed.
  
  #dm me in anyway you can and I'll try to explain it to you, 1 on 1 with proper iterations on slide!
