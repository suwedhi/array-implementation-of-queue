class Queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return(self.queue)==0
    def enqueue (self,item):
        self.queue.append(item)
    def dequeue (self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    def peek (self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]
    def size (self):
        return len (self.queue)
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueueing elements:",q.queue)
print("Dequeue elements:",q.dequeue())
print("Queue after dequeueing an elements:",q.queue)
print("Front elements:",q.peek())
print("Queue size:",q.size())

