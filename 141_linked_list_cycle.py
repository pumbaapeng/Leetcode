class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        l = r = head
        while (r and r.next):
            r = r.next.next
            l = l.next
            if r == l:
                return True
        return False
