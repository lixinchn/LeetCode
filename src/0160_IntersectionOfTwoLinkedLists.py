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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA, tempB = headA, headB
        lenA, lenB = 0, 0
        while tempA and tempA.next:
            tempA = tempA.next
            lenA += 1
        while tempB and tempB.next:
            tempB = tempB.next
            lenB += 1

        if tempA != tempB:
            return None

        tempA, tempB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                tempA = tempA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                tempB = tempB.next

        while True:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next


if __name__ == "__main__":
    solution = Solution()
    headA = ListNode.create([1])
    # tempA = headA
    # while tempA.val != 1:
    #     tempA = tempA.next
    headB = ListNode.create([1])
    # tempB = headB
    # while tempB.next:
    #     tempB = tempB.next
    # tempB.next = tempA

    node = solution.getIntersectionNode(headA, headB)
    print node
