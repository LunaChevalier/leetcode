#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.next == None and l2.next == None:
            return ListNode().next
        local_l1 = l1
        local_l2 = l2
        print(f'l1 {l1}')
        print(f'l2 {l2}')
        list_node_merge = ListNode()
        tmp = ListNode()
        while True:
            if local_l1 == None:
                tmp.val = local_l2.val
                list_node_merge.next = tmp
                list_node_merge.val = local_l2.val
                local_l2 = local_l2.next
            elif local_l2 == None:
                tmp.val = local_l1.val
                list_node_merge.next = tmp
                list_node_merge.val = local_l1.val
                local_l1 = local_l1.next
            elif local_l1.val <= local_l2.val:
                tmp.val = local_l1.val
                list_node_merge.next = tmp
                list_node_merge.val = local_l1.val
                local_l1 = local_l1.next
            else:
                tmp.val = local_l2.val
                list_node_merge.next = tmp
                list_node_merge.val = local_l2.val
                local_l2 = local_l2.next

            print(f'local_l1 {local_l1}')
            print(f'local_l2 {local_l2}')
            print(f'list_node_merge {list_node_merge}')
            if local_l1 == None and local_l2 == None: break
        
        return list_node_merge.next
# @lc code=end

