from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def returnLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}

        while head:
            prefix_sum += head.val
            if prefix_sum in prefix_sums:
                node = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum
                while node != head:
                    temp_sum += node.val
                    del prefix_sums[temp_sum]
                    node = node.next
                prefix_sums[prefix_sum].next = head.next
            else:
                prefix_sums[prefix_sum] = head
            head = head.next

        return dummy.next


# Test
head = returnLinkedList([1, 2, -3, 3, 1])
solution = Solution()
result = solution.removeZeroSumSublists(head)
while result:
    print(result.val, end=" ")
    result = result.next

print()
# head = returnLinkedList([1, 2, 3, -3, 4])
# solution = Solution()
# result = solution.removeZeroSumSublists(head)
# while result:
#     print(result.val, end=" ")
#     result = result.next

# print()
# head = returnLinkedList([1, 2, 3, -3, -2])
# solution = Solution()
# result = solution.removeZeroSumSublists(head)
# while result:
#     print(result.val, end=" ")
#     result = result.next
