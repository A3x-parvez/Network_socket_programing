import random
import time

def simulate_frame_transmission(total_frames):
    successful_frames = 0
    frame_id = 0

    while successful_frames < total_frames:
        print(f"\nAttempting to send frame {frame_id}...")
        time.sleep(1)  # Simulate waiting for the next time slot

        # Simulate sending the frame
        if random.choice([True, False]):  # Randomly decide if ACK is received or collision occurs
            print(f"Frame {frame_id} transmitted successfully.")
            successful_frames += 1
            frame_id += 1
        else:
            print("Collision occurred. Waiting for backoff period...")
            time.sleep(2)  # Simulate waiting for backoff period

    print("\nAll frames transmitted successfully.")

# Set the number of frames to transmit
total_frames = 5
simulate_frame_transmission(total_frames)
