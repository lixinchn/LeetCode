class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = head
        prev = None
        while head:
            temp = head
            if head.val == val:
                if new_head == head:
                    new_head = temp.next
                else:
                    prev.next = temp.next
            else:
                prev = temp
            head = head.next
        return new_head

if __name__ == "__main__":
    solution = Solution()
