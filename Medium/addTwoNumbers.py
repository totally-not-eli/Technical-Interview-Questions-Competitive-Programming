class Solution:
    def addTwoNumbers(self, l1,l2):
        new_ = ListNode()
        temporary_ = new_
        carry = 0

        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            sum = val1 + val2 + carry
            val = sum%10
            carry = sum//10

            temporary_.next = ListNode(val)
            temporary_ = temporary_.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return new_.next

