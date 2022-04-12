#check wether list is palindrome or not
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        cur = self.head
        if cur is None:
            self.head = new
            return

        while cur.next:
            cur = cur.next

        cur.next = new


    def __repr__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next

        return '[' + ','.join(nodes) + ']'

    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev
    
    def compareLists(self, second_half):
        cur1 = self.head
        cur2 = second_half

        while cur1 and cur2:
            if cur1.data == cur2.data:
                cur1 = cur1.next
                cur2 = cur2.next
            else:
                return 0

        if cur1 is None and cur2 is None:
            return 1

        return 0

    def isPalindrome(self):
        slow = fast = self.head
        mid = prev_slow = second_half = self.head

        while fast and fast.next:
           fast = fast.next.next
           prev_slow = slow
           slow = slow.next


        if fast:
            mid = slow
            slow = slow.next

        second_half = slow
        prev_slow.next = None
        second_half = self.reverse(second_half)
        res = self.compareLists(second_half)

        second_half = self.reverse(second_half)

        if mid:
            prev_slow.next = mid
            mid.next = second_half
        else:
            prev_slow.next = second_half

        return res
        

def printlist(second_half):
    while second_half:
        print(second_half.data)
        second_half = second_half.next
        


if __name__ == "__main__":
    input_str = 'abacaba'
    ll = LinkedList()
    for i in input_str:
        ll.append(i)

    result = ll.isPalindrome()
    if(result):
        print('palindrome')
    else:
        print('not palindrome')
