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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        len_list = 0
        temp = head
        while temp:
            len_list += 1
            temp = temp.next

        if len_list == 0:
            return head

        if k >= len_list:
            k %= len_list

        if k == 0:
            return head

        temp = head
        index = 0
        while temp:
            index += 1
            if index == len_list - k:
                new_head = temp.next
                temp.next = None
                break
            temp = temp.next

        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head

        return new_head


if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([])
    head = solution.rotateRight(head, 1)
    head._print()
        