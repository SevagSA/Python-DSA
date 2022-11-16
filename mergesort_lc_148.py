'''
Mergesort algorithm implementation
This is the solution to LeetCode 148.
'''


from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None) -> None:
        self.val = val
        self.next = next


class Solution:

    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is empty, return head, i.e. None
        # if head.next is empty, i.e. 1 element in list, return head
        if not head or not head.next:
            return head

        # split the list into two halves
        left_head = head
        # will eventually be the right list's head
        right_head = self.get_mid(head)
        # get the right list's head, which is the next node of the middle element
        tmp = right_head.next
        # split the left list from the right by setting the .next element
        # of the midpoint to `None`
        right_head.next = None
        # `tmp` is now the start of the right list, i.e. its head
        right_head = tmp

        # Recurse with the newly splited lists
        # This will recurse until there is 1 element in each list (see the first
        # `if` statement of this function)
        left_head = self.sort_list(left_head)
        right_head = self.sort_list(right_head)

        # Recursion will finish here. By this point, the lists are splitted
        # so we just need to merge them
        return self.merge(left_head, right_head)

    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left_head, right_head):
        tail = start = ListNode()
        while left_head and right_head:
            if left_head.val < right_head.val:
                tail.next = left_head
                left_head = left_head.next
            else:
                tail.next = right_head
                right_head = right_head.next
            tail = tail.next
        # At this point, it is possible that either left_head or right_head
        # is not empty. If so, they should be added to the linked list. This
        # happens when the lists have a different number of elements, i.e.
        # when the intial list that we want to sort has an odd number of elements.
        if left_head:
            tail.next = left_head
        if right_head:
            tail.next = right_head
        # `start` is a pointer to the first `ListNode()` element, same as `tail`.
        # `tail` was used to add the list's elements in order.
        # `tail` added the elements by doing `tail.next = {element}`
        # That means that `tail.val` is 0 (default value assigned in `ListNode`
        # constructor) for the first call.
        # So we don't want to return the current value, i.e `tail.val`, but `tail.next`.
        # However, since we used `tail` to iterate through the linked list by doing
        # `tail = tail.next`, tail is no longer pointing to the start, but to the 'tail'
        # of the list, hence its name.
        # So, the `start` variable was used to keep a pointer to the first `ListNode()`
        # element, and since `start` was not iterated, we can simply do start.next to get the
        # head of the sorted linked list.
        return start.next
