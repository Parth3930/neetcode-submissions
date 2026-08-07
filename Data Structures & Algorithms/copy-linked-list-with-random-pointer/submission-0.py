class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldC = { None : None }

        curr = head
        while curr:
            copy = Node(curr.val)
            oldC[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldC[curr]
            copy.next = oldC[curr.next]
            copy.random = oldC[curr.random]
            curr = curr.next

        return oldC[head]