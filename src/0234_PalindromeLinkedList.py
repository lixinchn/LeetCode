class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        count = 0
        temp = head
        middle = head
        while temp:
            count += 1
            if count % 2 == 0:
                middle = middle.next
            temp = temp.next

        
        pre = middle
        temp2 = middle.next if middle else None
        while temp2:
            temp3 = temp2.next
            temp2.next = pre
            pre = temp2
            temp2 = temp3
        if middle:
            middle.next = None

        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True


solution = Solution()
