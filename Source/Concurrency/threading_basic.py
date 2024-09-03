import threading, time

#def function_thread(one, two, three):
def function_thread():
    print('starting thread:')
    time.sleep(3)
    print('exiting thread:')
    
#first_thread = threading.Thread(target=function_thread, args=('first', 'second'), kwargs={'three': 'third'})
first_thread = threading.Thread(target=function_thread)
print(first_thread.is_alive())
first_thread.start()
first_thread.join() # this will block first thread, until it is released or executed.
print(first_thread.is_alive())
