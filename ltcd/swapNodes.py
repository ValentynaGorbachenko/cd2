# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    node = head;
    # print (head)
    while node.next.next:
        # print (node.val, node.next.val)
        temp = node.next
        print('2 ' ,temp.val)
        node.next = temp.next
        print('3 ',node.next.val)
        temp.next = node
        print('1 ',temp.next.val)
        node = node.next
        try: 
            print('3 ',node.val)
        except:
            continue
    temt = node.next
    node.next = node.next.next
    node = node.next

n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
print(n.val, n.next.val, n.next.next.val, n.next.next.next.val)
swapPairs(n)
# print(n.val, n.next.val, n.next.next.val)