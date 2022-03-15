class MyCircularQueue:

    def __init__(self, k: int):
        

    def enQueue(self, value: int) -> bool:
        

    def deQueue(self) -> bool:
        

    def Front(self) -> int:
        

    def Rear(self) -> int:
        

    def isEmpty(self) -> bool:
        

    def isFull(self) -> bool:
        


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
