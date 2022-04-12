#find the kth small element in array

def merge(ar, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    l1 = [0] * n1
    l2 = [0] * n2

    for i in range(n1):
        l1[i] = ar[i+ low]

    for j in range(n2):
        l2[j] = ar[j + mid +1]

    i = 0
    j = 0
    k = low

    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            ar[k] = l1[i]
            i +=1
            k +=1
        else:
            ar[k] = l2[j]
            j +=1
            k +=1

    while i < n1:
        ar[k] = l1[i]
        i +=1
        k +=1

    while j<n2:
        ar[k] = l2[j]
        j +=1
        k +=1

def method1(ar, low, high):
    if low < high:
        mid = (low + (high -1))//2

        method1(ar, low, mid)
        method1(ar, mid+1, high)
        merge(ar, low, mid, high)

import sys

class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 
  
# Driver Code 
if __name__ == "__main__": 
      
    print('The minHeap is ') 
    minHeap = MinHeap(15) 
    minHeap.insert(7) 
    minHeap.insert(10) 
    minHeap.insert(4) 
    minHeap.insert(3) 
    minHeap.insert(20) 
    minHeap.insert(15) 
    minHeap.minHeap() 
  
    minHeap.Print()
    k = int(input('enter k'))
    for i in range(k):
        if i == k-1:
            print("The Min val is " + str(minHeap.remove()))
            break
        minHeap.remove()
