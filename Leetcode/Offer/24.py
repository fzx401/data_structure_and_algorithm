"""
经典翻转链表：
维护pre指针指向None
令cur指向头节点
维护一个tmp指向cur的next
令cur.next指向pre
更新pre为cur
令cur指向tmp
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            #  以上两步完成后，cur本体不变，将原本的cur.next储存起来，然后用pre更新cur.next
            pre = cur
            cur = tmp
        return pre

from DataStructures.generate_link_list import generate_link_list

l = generate_link_list([1, 2, 3, 4, 5])
s = Solution()
print(s.reverseList(l))
