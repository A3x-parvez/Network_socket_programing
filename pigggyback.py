# import time

# def send_data(sender_id, receiver_id, data, piggyback_ack):
#     message = f"Sender {sender_id} sends data {data} to Receiver {receiver_id}"
#     if piggyback_ack:
#         message += " (with piggybacked ACK)"
#     print(message)

# def piggybacking_simulation(data_packets):
#     ack = 0  # Track acknowledgment number
#     for i, packet in enumerate(data_packets):
#         piggyback_ack = (i > 0)
#         send_data(1, 2, packet, piggyback_ack)
        
#         # Simulate acknowledgment
#         print(f"Receiver 2 received data {packet} and sends ACK {ack}")
#         ack += 1
#         time.sleep(1)  # Simulate delay

# # Sample data packets
# data_packets = [10, 20, 30, 40, 50]

# print("Starting Piggybacking Simulation...")
# piggybacking_simulation(data_packets)
# print("Simulation Complete.")


class pack:
    sender = 0
    reciver = 0
    data ="Data"
    
