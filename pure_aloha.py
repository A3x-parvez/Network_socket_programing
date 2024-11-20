import random
import time

# Initialize parameters
total_frames = 10  # Total number of frames to send
successful_frames = 0  # Counter for successfully sent frames
frame_id = 0  # Current frame ID to send

# Function to simulate sending a frame
def send_frame(frame_id):
    print(f"Sending frame {frame_id}...")
    # Randomly determine if the frame transmission is successful (50% chance)
    return random.choice([True, False])

# Function to simulate waiting for acknowledgment
def wait_for_ack():
    time.sleep(0.5)  # Simulating a brief wait
    return send_frame(frame_id)

# Main loop to send all frames
while successful_frames < total_frames:
    # Send the current frame and wait for acknowledgment (ACK)
    ack_received = wait_for_ack()
    
    if ack_received:
        # Frame successfully transmitted
        print(f"Frame {frame_id} transmitted successfully.")
        successful_frames += 1
        frame_id += 1
    else:
        # Collision occurred
        print(f"Collision occurred for frame {frame_id}.")
        # Wait for a random backoff period (1-3 seconds)
        backoff_time = random.randint(1, 3)
        print(f"Waiting for backoff period: {backoff_time} seconds...")
        time.sleep(backoff_time)

print("All frames transmitted successfully!")
