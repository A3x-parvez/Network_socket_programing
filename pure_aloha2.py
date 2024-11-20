import random
import time 

frame = int(input("Enter frame no : "))
frame_id = 0
frame_transmitted = 0

def send_frame(frame_id):
    print(f"Sending frame {frame_id}")
    time.sleep(1)
    return random.choice([False,True])

def send_akc():
    time.sleep(1)
    return send_frame(frame_id)

while frame_transmitted < frame:
    
    akc = send_akc()
    
    if akc :
        print(f"Sucessfully send frame {frame_id}")
        time.sleep(1)
        frame_id=frame_id+1
        frame_transmitted=frame_transmitted+1
    else:
        print(f"Collusion occur for frame {frame_id} ")
        backoff = random.randint(1,3)
        print(f"Wait for {backoff} sec and send again...")
        time.sleep(backoff)
        
print("All frame transmitted.")