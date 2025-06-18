import threading
import time

pause_resume_event = threading.Event()
stop_event = threading.Event()

def print_numbers():
    for x in range(1000):
        if stop_event.is_set():
            return
        pause_resume_event.wait()
        print(x)
        time.sleep(0.2)
            
my_thread = threading.Thread(target=print_numbers)      
print('Type p and enter to pause/resume')      
print('Type x and enter to stop')      
input('Press enter to start...')      
pause_resume_event.set()
my_thread.start()

while True:
    user_command = input().strip().lower()
    if user_command == 'x':
        stop_event.set()
        my_thread.join()
        print('EXITING')
        break
    elif user_command == 'p':
        if  pause_resume_event.is_set():
            pause_resume_event.clear()
            print('PAUSED')
        else:
            print('RESUMED')
            pause_resume_event.set()