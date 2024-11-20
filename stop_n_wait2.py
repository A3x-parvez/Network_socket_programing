import time

def stopNwait(frames):
    i=0
    j=0
    remain_frame = frames
    while remain_frame > 0:
        print(f"Sending frame {i}")
        i=i+1
        time.sleep(1)
        if i%2 ==0:
            print(f"{i-1} Frame lost ......")
            time.sleep(2)
            print(f"Resend the frame {i-1}")
    
        print(f"Acknowledgement recived for {j}")
        j=j+1
        remain_frame = remain_frame-1       
    print("Sending complete.")     
    
frame = int(input("Enter number of frames you want to send : "))
stopNwait(frame)
