class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        nodes = []
        while cur:
            nodes.append(repr(cur.data))
            cur = cur.next

        return '['+','.join(nodes)+']'

    def append(self, data):
        node = Node(data)
        cur = self.head
        if cur is None:
            self.head = node
            return
        
        while cur.next:
            cur = cur.next
        cur.next = node


    def insertfirst(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def size(self):
        cur = self.head
        count =0
        while cur:
            count +=1
            cur = cur.next
        return count
    
    def insert(self, pos, data):
        size = self.size()
        node = Node(data)
        cur = self.head
        for i in range(1,size):
            if i != (pos-1):
                cur = cur.next
            else:
                break
        node.next = cur.next
        cur.next = node

    def delete(self, key):
        cur = self.head
        prev = None
        if self.head is None:
            print("No elements to delete")
            return
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None and prev is not None:
            print("Element not found")
            return
        elif prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
            

    def deletelist(self):
        self.head = None

    def datpos(self, pos):
        if self.head is None:
            print("No elements in list")
            return
        prev = None
        cur = self.head
        i = 0
        while cur and i != pos:
            prev = cur
            cur = cur.next
            i +=1

        if cur is None and prev is not None:
            print("No element in list")
            return
        elif prev is None:
            print('not a valid position')
            return
        else:
            prev.next = cur.next

    def reverse(self):
        cur = self.head
        next = None
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def bubblesort(self):
        end = None
        while end != self.head:
            cur = self.head
            while cur.next != end:
                next = cur.next
                if cur.data > next.data:
                    cur.data, next.data = next.data, cur.data
                cur = cur.next

            end = cur

    def linkswap(self):
        end = None
        while end != self.head:
            cur = self.head
            prev = self.head

            while cur.next != end:
                next = cur.next

                if cur.data > next.data:
                    cur.next = next.next
                    next.next = cur
                    if cur!= self.head:
                        prev.next = next
                    else:
                        self.head = next
                    cur, next = next, cur
                prev = cur
                cur = cur.next
            end = cur


    def merge_newlist(self, l, l2):
        newlist = LinkedList()
        p = l.head
        q = l2.head
        if p.data <= q.data:
            newlist.head = Node(p)
            p = p.next
        else:
            newlist.head = Node(q)
            q = q.next

        while p is not None and q is not None:
            if p.data < q.data:
                element = p.data
                p = p.next
            else:
                element = q.data
                q = q.next

            newlist.append(element)

        while p is not None:
            newlist.append(p.data)
            p = p.next

        while q is not None:
            newlist.append(q.data)
            q = q.next

        print(newlist)
    
    def selection_sort(self):
        cur = self.head

        while(cur):
            minn = cur
            temp = cur.next

            while(temp):
                if minn.data > temp.data:
                    minn = temp
                
                temp = temp.next

            cur.data, minn.data = minn.data, cur.data

            cur = cur.next

    def getNthnode(self, ind):
        cur = self.head
        for i in range(0, self.size()):
            if i == ind:
                return cur.data
            cur = cur.next

    def sortedInsert(self, data):
        new_node = Node(data)
        cur = self.head
        while(cur):
            if data < cur.data:
                break
            prev = cur
            cur = cur.next

        new_node.next = prev.next
        prev.next = new_node

    def splitlist(self):
        first = LinkedList()
        second = LinkedList()
        list_size = self.size()
        if list_size%2 == 0:
            count = list_size//2
        else:
            count  = (list_size//2)+1
        cur = self.head
        for i in range(1, count):
            cur = cur.next
        slow = self.head
        fast = cur.next
        while slow and fast:
            first.append(slow)
            second.append(fast)
            slow = slow.next
            fast = fast.next
        
        if slow is not None:
            first.append(slow)
            slow = slow.next

        print(first)
        print(second)
        
    def removeduplicate(self):
        distinct = []
        cur = self.head
        prev = None
        while cur:
            if cur.data not in distinct:
                distinct.append(cur.data)
                prev = cur
            else:
                prev.next = cur.next
                cur = prev       
            
            cur = cur.next
        
    def removeduplicate1(self):
        cur = self.head
        while cur.next:
            if cur.data == cur.next.data:
                new = cur.next.next
                cur.next = None
                cur.next = new
            else:
                cur = cur.next

    def moveNode(self,second):
        cur = self.head
        if cur is None:
            return print('the source list is empty')
        
        head = second.head
        second.head = cur.next
        cur.next = head
        print(self)
        print(second)

    def alternatesplit(self):
        a = LinkedList()
        b = LinkedList()
        cur = self.head
        while cur:
            a.append(cur.data)
            b.append(cur.next.data)
            cur = cur.next.next
        
        print(a, b)
 
    #remove all occurences of duplicates, i.e [1,1,2,4,4] output should be [2]
    def removeall(self):
        cur = self.head
        head =prev = Node(None)
        head.next =cur
        while cur and cur.next:
            if cur.data == cur.next.data:
                while(cur and cur.next) and cur.data==cur.next.data:
                    cur = cur.next
                
                cur = cur.next
                prev.next = cur
            
            else:
                prev = prev.next
                cur = cur.next
        return head.next

    def removeAllDuplicates(self, temp): 
          
        # temp is head node of linkedlist 
        curr = temp 
        # print(' print something') 
        head = prev = Node(None) 
        head.next = curr 
  
        # Here we use same as we do in removing  
        # duplicates and only extra thing is that 
        # we need to remove all elements  
        # having duplicates that we did in 30-31 
        while curr and curr.next: 
              
            # until the current value and next  
            # value are same keep updating the current value 
            if curr.data == curr.next.data: 
                while(curr and curr.next and 
                      curr.data == curr.next.data): 
                    curr = curr.next
                      
                    # still one of duplicate values left 
                    # so point prec to curr 
                curr = curr.next
                prev.next = curr 
            else: 
                prev = prev.next
                curr = curr.next
        return head.next


    def countduplicates(self):
        cur = self.head
        count = 0 
        while cur.next:
            if cur.data == cur.next.data:
                count +=1
                print("cur is {0} cur.next is {1}".format(cur.data, cur.next.data))
                cur.next = cur.next.next
            else:
                cur = cur.next
        return print(count)

    #replace duplicate values with n+1, n+2, n+3 ....
    def replaceduplicate(self):
        dic = {}
        cur = self.head
        maxnum = -234
        #traverse all nodes in linked list and store the frequency in dictionary
        while cur:
            c =0
            if cur.data not in dic.keys():
                dic[cur.data] =  c +1
            else:
                dic[cur.data] = dic[cur.data] + 1
                
            if maxnum < cur.data:
                maxnum = cur.data
            cur = cur.next

        cur = self.head

        #traverse and replace the duplicates
        while cur:

            if dic[cur.data] >1:
                dic[cur.data] = -1

            elif dic[cur.data] == -1:
                maxnum +=1
                cur.data = maxnum

            cur = cur.next

        print(self)

    #find the max sum sub list by comparing two lists with common node
    # example List1 =  1->3->30->90->120->240->511
    #List2 =  0->3->12->32->90->125->240->249 Output : 1->3->12->32->90->125->240->511
    def finalmaxsumlist(self, a, b):
        result = None
        prev1 = a
        prev2 = b
        cur1 = a
        cur2 = b

        while cur1 != None or cur2 !=None:
            sum1 = 0
            sum2 = 0
            while cur1 != None and cur2 !=None and cur1.data != cur2.data:
                if cur1.data < cur2.data:
                    sum1 +=cur1.data
                    cur1 = cur1.next
                else:
                    sum2 += cur2.data
                    cur2 = cur2.next


            if cur1 == None:
                while cur2 !=None:
                    sum2 +=cur2.data
                    cur2 = cur2.next

            if cur2 == None:
                while cur1 !=None:
                    sum1 +=cur1.data
                    cur1 = cur1.next

            if prev1 == a and prev2 == b:
                result = prev1 if (sum1 > sum2) else prev2
            else:
                if sum1 > sum2:
                    prev2.next = prev1.next
                else:
                    prev1.next = prev2.next
            prev1 = cur1
            prev2 = cur2

            if cur1 != None:
                cur1 = cur1.next

            if cur2 != None:
                cur2 = cur2.next

        while result !=None:
            print(repr(result.data))
            result = result.next

    def delete_k_node(self, k):
        cur = self.head
        count = 1
        prev = Node(None)
        while cur:
            if count == k:
                prev.next = cur.next
                count = 0
            
            prev = cur
            count +=1
            cur = cur.next
        
        return self.head

    def delete_n_node_from_end(self, n):
        cur = self.head
        size = self.size() - n
        count = 0
        prev = None
        while cur:
            if count == size:
                prev.next = cur.next
            
            count  +=1
            prev = cur
            cur = cur.next

    def rotate_n_node(self, n):
        c = 1
        cur = self.head
        while cur:
            next = cur.next
            if c == n:
                break

            c +=1
            cur = cur.next
        
        temp = cur
        while temp.next:
            temp = temp.next
        
        print(temp.data)

        temp.next = self.head
        cur.next = None
        self.head = next


if __name__=="__main__":
    l = LinkedList()
    l.append(1)
    l.append(3)
    l.append(30)
    l.append(90)
    l.append(120)
    l.append(240)
    l.append(511)
    print(l)
    l.rotate_n_node(4)
    print(l)
    
    

