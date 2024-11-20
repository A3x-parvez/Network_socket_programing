import time 
import random

def send_frames(total_frame):
    frame = total_frame
    frame_send = 0
    frame_id = 0 
    
    while frame > frame_send:
        print("\nWating for next time slot.")
        time.sleep(1)
        print(f"Sending frame {frame_id}")
        
        if (random.choice([True,False])):
            print(f"Frame {frame_id} send successfully.")
            frame_send = frame_send+1
            frame_id = frame_id+1
        else:
            print(f"Collusion occur for frame {frame_id} wait for a backoff time.")   
            time.sleep(2)
            
    print("All frame send Successfully.")
    
f = int(input("Enter the num of frame : "))
send_frames(f)