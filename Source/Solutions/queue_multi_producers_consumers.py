import threading
from collections import deque

class MultiProducersConsumersQueue:
    def __init__(self):
        self.queue = deque()
        self.condition = threading.Condition()
        
    def enqueue(self, item):
        with self.condition:
            self.queue.append(item)
            # Notify waiting consumer, that item is available.
            self.condition.notify()
            
    def dequeue(self):
        with self.condition:
            while not self.queue:
                # wait until an item is available.
                self.condition.wait()
            return self.queue.popleft()

def producer(queue, name):
    for i in range(10):
         queue.enqueue(i)
         print(f"{name} Produced {i}")
         
def consumer(queue, name):
    while True:
        item = queue.dequeue()
        print(f"{name} Consumed {item}")
        

queue = MultiProducersConsumersQueue()
first_producer = threading.Thread(target=producer, args=(queue, "First"))
first_producer.start()
first_consumer = threading.Thread(target=consumer, args=(queue, "First"))
first_consumer.start()
second_producer = threading.Thread(target=producer, args=(queue, "Second"))
second_producer.start()
second_consumer = threading.Thread(target=consumer, args=(queue, "Second"))
second_consumer.start()
