'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


def removeElements(head, val):
    prev = None
    # curr = head.head
    curr = head

    if head == None:
        return head

    while curr.next:
        # print ('current ',curr.val)
        if curr.val == val:
            if prev:

                prev.next = curr.next
                curr = prev.next
                
            else:
                head = curr.next
                # head.head = curr.next
                curr = head
                # curr = head.head      

        else:
            prev = curr
            curr = curr.next

    if curr.val == val:
        if prev:
            prev.next = None
        else:
            head = None
        
    cur = head
    # cur = head.head
    while cur:
        print(cur.val)
        cur = cur.next

        
node = ListNode(2)
node.next = ListNode(1)
node.next.next = ListNode(2)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(3)
node.next.next.next.next.next = ListNode(2)
node.next.next.next.next.next.next = ListNode(5)
node.next.next.next.next.next.next.next = ListNode(2)
node.next.next.next.next.next.next.next.next = ListNode(2)
# h = LinkedList(node)
# removeElements(node, 2)
removeElements(ListNode(1), 1)


'''
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow,fast = dummy,head
        while fast:
            if fast.val == val:
                slow.next = fast.next
                fast = slow.next
            else:
                fast = fast.next
                slow = slow.next
        return dummy.next
'''


