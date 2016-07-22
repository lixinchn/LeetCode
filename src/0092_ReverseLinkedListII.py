class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(arr):
        head = None
        this = None
        for val in arr:
            node = ListNode(val)
            if not head:
                head = node
                this = node
                continue

            this.next = node
            this = node
        return head

    def _print(self):
        temp = self
        result = ''
        while temp:
            result += str(temp.val) + ','
            temp = temp.next
        print result

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        index = 1
        ret_head = head
        first_node, prev_first_node = None, None
        prev_node, this_node = None, None
        while head:
            head_next = head.next

            if index == m:
                first_node = head
                prev_node = head
            elif index > m and index <= n:
                this_node = head
                this_node.next = prev_node
                prev_node = this_node
            
            if index == n and prev_first_node:
                prev_first_node.next = head
            if index == n + 1:
                first_node.next = head

            if not first_node:
                prev_first_node = head

            index += 1
            head = head_next

        if index <= n + 1:
            first_node.next = None
        if m == 1:
            ret_head = prev_node
        return ret_head


if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([3,5])
    head = solution.reverseBetween(head, 1, 2)
    head._print()

    head = ListNode.create([1,2,3])
    head = solution.reverseBetween(head, 2, 3)
    head._print()