import threading, time

pause_resume_event = threading.Event()
stop_event = threading.Event()

def analyze_things():
    for x in range(1000):
        if stop_event.is_set():
            return
        else:
            pause_resume_event.wait()
            print(x)
            time.sleep(0.2)
            
my_thread = threading.Thread(target=analyze_things)      
my_thread.start()

print('Type p to pause/resume')      
print('Type x to stop')      
input('Press enter to start...')      

pause_resume_event.set()

while True:
    user_command = input()
    if user_command == 'x':
        stop_event.set()
        print('EXITING')
        exit()
    elif user_command == 'p':
        if  pause_resume_event.is_set():
            pause_resume_event.clear()
            time.sleep(0.2)
            print('PAUSED')
        else:
            time.sleep(0.2)
            print('RESUMED')
            pause_resume_event.set()