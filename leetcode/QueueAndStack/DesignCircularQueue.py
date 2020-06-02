class MyCircularQueue:
    q=[]
    Front=0
    Rear=0

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q=[-1]*k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.Rear != -1:
            return False

        self.q[self.Rear]=value
        self.Rear=(self.Rear+1)%len(self.q)

        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        print(self.q)
        target=self.q[self.Front]
        self.q[self.Front]=-1
        self.Front=(self.Front+1)%len(self.q)

        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.Front

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.Rear

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.Front != self.Rear:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.Front == self.Rear:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

circularQueue = MyCircularQueue(3); #// set the size to be 3
circularQueue.enQueue(1); # // return true
circularQueue.enQueue(2);  #// return true
circularQueue.enQueue(3);  #// return true
circularQueue.enQueue(4);  #// return false, the queue is full
circularQueue.Rear();  #// return 3
circularQueue.isFull();  #// return true
circularQueue.deQueue();  #// return true
circularQueue.enQueue(4);  #// return true
circularQueue.Rear(); # // return 4