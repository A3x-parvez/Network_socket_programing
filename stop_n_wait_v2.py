import time
import random

# Function to simulate Stop-and-Wait Protocol with acknowledgment timeout and retry mechanism
def stop_and_wait_protocol(num_frames):
    frame_counter = 0  # Frame counter
    acknowledgment_counter = 0  # Acknowledgment counter
    remaining_frames = num_frames
    max_retries = 3  # Max retries for a lost frame
    timeout = 2  # Timeout duration in seconds

    while remaining_frames > 0:
        print(f"Sending frame {frame_counter}")
        
        # Simulate sending frame and randomly decide if it's lost
        frame_lost = random.choice([True, False])

        if frame_lost:
            print(f"Frame {frame_counter} lost. Retrying...")
            retries = 0
            success = False

            # Retry mechanism for lost frame
            while retries < max_retries and not success:
                retries += 1
                print(f"Retry {retries} for frame {frame_counter}")
                time.sleep(1)  # Simulate wait before retry
                
                # Simulate another random chance of success in retry
                if random.choice([True, False]):
                    success = True
                    print(f"Frame {frame_counter} sent successfully on retry {retries}")
                else:
                    print(f"Retry {retries} failed")

            if not success:
                print(f"Failed to send frame {frame_counter} after {max_retries} retries. Aborting...")
                break  # Abort if max retries are reached
        else:
            print(f"Frame {frame_counter} sent successfully")

        # Simulate acknowledgment with timeout
        start_time = time.time()
        ack_received = False
        
        while not ack_received:
            # Simulate random acknowledgment success/failure
            if random.choice([True, False]):
                ack_received = True
                print(f"Acknowledgment received for frame {acknowledgment_counter}")
                acknowledgment_counter += 1
            elif time.time() - start_time > timeout:
                print(f"Acknowledgment timeout for frame {frame_counter}. Resending...")
                break  # Break the acknowledgment loop to resend the frame

        # Proceed to the next frame if acknowledgment was received
        if ack_received:
            frame_counter += 1
            remaining_frames -= 1

    print("End of Stop-and-Wait protocol")

# Input number of frames
num_frames = int(input("Enter the number of frames to send: "))
stop_and_wait_protocol(num_frames)
