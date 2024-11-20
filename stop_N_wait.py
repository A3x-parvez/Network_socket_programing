import time

# Function to simulate Stop-and-Wait Protocol
def stop_and_wait_protocol(num_frames):
    i = 0  # Frame counter
    j = 0  # Acknowledgment counter
    remaining_frames = num_frames

    while remaining_frames > 0:
        # Send frame
        print(f"Sending frame {i}")
        i += 1

        # Simulate a condition for resending a frame
        if i % 2 == 0:
            print("Frame lost, resending...")
            time.sleep(1)  # Wait for 1 second before resending
            print(f"Resending frame {i - 1}")

        # Print acknowledgment
        print(f"Acknowledgment received for frame {j}")
        j += 1

        # Decrement remaining frames
        remaining_frames -= 1

    print("End of Stop-and-Wait protocol")

# Input number of frames
num_frames = int(input("Enter the number of frames to send: "))
stop_and_wait_protocol(num_frames)
