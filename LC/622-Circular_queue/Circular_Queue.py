class MyCircularQueue_2:
    def __init__(self, k: int):
        self._series = tuple([[] for _ in range(k)]);
        self.capacity = k;
        self._front = 0;
        self._rear = 0;
        self.size = 0;

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False;
        if self.size == 0:
            self.front_obj.append(value);
        else:
            self._rear = self.get_next_r_idx();
            self.rear_obj.append(value);
        self.size += 1; 
        print(self._series, self.size, "head:", self._front, "rear", self._rear);
        return (True);

    def deQueue(self) -> bool:
        if self.size == 0:
            return False;
        self.front_obj.pop();
        self._front = self.get_next_f_idx();
        self.size -=1;
        print(self._series, self.size, "head:", self._front, "rear", self._rear);
        return True;

# PASS
    def isFull(self) -> bool:
        return (self.size == self.capacity);

    def get_next_f_idx(self):
        f = self._front;
        return 0 if (f + 1 == self.capacity) else f + 1;

    def get_next_r_idx(self):
        r = self._rear;
        return 0 if (r + 1 == self.capacity) else r + 1;

    def isEmpty(self) -> bool:
        return False if self.size else True;

    def Front(self) -> int:
        ret = self.front_obj;
        return (ret[0] if ret else -1);

    def Rear(self) -> int:
        ret = self.rear_obj;
        return (ret[0] if ret else -1);

    @property
    def front_obj(self) -> list:
        ret = self._series[self._front];
        assert(type(ret) == list);
        return (ret);

    @front_obj.setter
    def front_obj(self, v):
        self.front_obj[0] = v;

    @property
    def rear_obj(self) -> list:
        ret = self._series[self._rear];
        assert(type(ret) == list);
        return (ret);

    @rear_obj.setter
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

def test():
    myCircularQueue = MyCircularQueue_2(3);
    assert(myCircularQueue.enQueue(1) == True)
    assert(myCircularQueue.enQueue(2) == True) #  True
    assert(myCircularQueue.enQueue(3) == True) #  True
    assert(myCircularQueue.enQueue(4) == False) #  False
    assert(myCircularQueue.Rear() == 3)        #  3
    assert(myCircularQueue.isFull() == True)   #  True
    assert(myCircularQueue.deQueue() == True)  #  True
    assert(myCircularQueue.deQueue() == True)  #  True
    assert(myCircularQueue.enQueue(4) == True) #  True
    assert(myCircularQueue.enQueue(4) == True) #  True
    assert(myCircularQueue.deQueue() == True)  #  True
    assert(myCircularQueue.Rear() == 4)        #  4

if __name__ == "__main__":
    test();
        
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
