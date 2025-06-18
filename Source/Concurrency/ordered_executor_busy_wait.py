# self.step < n: pass loops waste CPU time and refers busy waiting.
# using threading.Event, threading.Condition or Semaphore to allow the thread to wait efficiently without consuming CPU.

import threading

class OrderedExecutor:
    def __init__(self):
        self.step = 0

    def first(self):
        print("first", end=' ')
        self.step = 1
        
    def second(self):
        while self.step < 1:
            pass
        print("second", end=' ')
        self.step = 2
        
    def third(self):
        while self.step < 2:
            pass
        print("third", end=' ')
        
    def random(self):
        print("random", end=' ')
        
executor = OrderedExecutor()

# Start threads in arbitrary order
threads = [
    threading.Thread(target=executor.random),
    threading.Thread(target=executor.third),
    threading.Thread(target=executor.second),
    threading.Thread(target=executor.random),
    threading.Thread(target=executor.first)
]

for t in threads:
    t.start()
for t in threads:
    t.join()

