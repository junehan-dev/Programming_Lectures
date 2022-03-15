class MyCircularQueue:
    def __init__(self, k: int):
        self._series = Tuple([[] for _ in range(k)]);
        self.capacity = k;
        self._front = 0;
        self._rear = 0;

    def enQueue(self, value: int) -> bool:
        """
        if self.isFull():
            return False;
        """
        pass

    def deQueue(self) -> bool:
        """
        ret = self.front_obj.pop();
        return front.pop()
        """

    def isFull(self) -> bool:
        """IF REAR NEXT IS FRONT? -> THEN FULL.
        f = self.Front();
        r = self.Rear();

        if (f < r):
            return True if (r-1 == f) else False;
        if (f > r):
            return True if (f-1 == r) else False;
        return False;
        """
        pass

# PASS
    def isEmpty(self) -> bool:
        """IF FRONT EQUAL REAR -> THEN EMPTY.
        """
        return (self._front == self._rear);

    def Front(self) -> int:
        return (self.front_obj[0]);

    def Rear(self) -> int:
        return (self.rear_obj[0]);

    @property
    def front_obj(self) -> list:
        ret = self_series[self._front];
        assert(type(ret) == list);
        return (ret);

    @front_obj.setter(self, v):
    def front_obj(self, v):
        self.front_obj[0] = v;

    @property
    def rear_obj(self) -> list:
        ret = self_series[self._rear];
        assert(type(ret) == list);
        return (ret);

    @rear_obj.setter(self, v):
    def rear_obj(self, v):
        self.rear_obj[0] = v;

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

def test()
    MyCircularQueue myCircularQueue = MyCircularQueue(size);
    assert(myCircularQueue.enQueue(1) == True)
    assert(myCircularQueue.enQueue(2) == True) #  True
    assert(myCircularQueue.enQueue(3) == True) #  True
    assert(myCircularQueue.enQueue(4) == False) #  False
    assert(myCircularQueue.Rear() == 3)        #  3
    assert(myCircularQueue.isFull() == True)   #  True
    assert(myCircularQueue.deQueue() == True)  #  True
    assert(myCircularQueue.enQueue(4) == True) #  True
    assert(myCircularQueue.Rear() == 4)        #  4

if __name__ == "__main__":
    #test();
        
"""
Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
"""
