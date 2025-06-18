import threading

class OrderedExecutor:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()
    
    def first(self):
        print("first", end=' ')
        self.first_done.set()
        
    def second(self):
        self.first_done.wait()  # This will block first, unless first is set() again.
        print("second", end=' ')
        self.second_done.set()
        
    def third(self):
        self.second_done.wait()
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
