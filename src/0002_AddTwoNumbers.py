# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_r(self):
        while (self):
            print self.val
            self = self.next

    @staticmethod
    def create(lst):
        start = temp = ListNode(lst[0])
        for i in range(1, len(lst)):
            node = ListNode(lst[i])
            temp.next = node
            temp = node
        return start

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_l = point_l = ListNode(0)
        carry_flag = 0
        while True:
            digit1 = l1.val if l1 and l1.val else 0
            digit2 = l2.val if l2 and l2.val else 0
            digit3 = digit1 + digit2 + carry_flag
            point_l.val = digit3 % 10
            carry_flag = digit3 / 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2:
                if carry_flag:
                    temp_l = ListNode(carry_flag)
                    point_l.next = temp_l
                    point_l = temp_l
                break
            temp_l = ListNode(0)
            point_l.next = temp_l
            point_l = temp_l
        return ret_l

if __name__ == "__main__":
    a = (2, 4, 3)
    b = (5, 6, 4)
    lst_a = ListNode.create(a)
    lst_b = ListNode.create(b)
    # lst_a.print_r()
    # lst_b.print_r()
    solution = Solution()
    ret_lst = solution.addTwoNumbers(lst_a, lst_b)
    ret_lst.print_r()

        