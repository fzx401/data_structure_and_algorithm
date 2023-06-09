class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def generate_link_list(nums:list):
    i = 1
    cur = ListNode(nums[0])
    head = cur
    while i < len(nums):
        cur.next = ListNode(nums[i])
        # print('cur_before')
        # print(id(cur))
        # print('head_before')
        # print(id(head))
        cur = cur.next  # 在此时cur已经变成了一个新变量
        # print('cur_after')
        # print(id(cur))
        # print('head_after')
        # print(id(head))
        i += 1
    return head