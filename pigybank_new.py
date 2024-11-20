import time

class PiggybackProtocol:
    def __init__(self):
        """Initialize protocol with default data packets"""
        self.data_packets = [10, 20, 30, 40, 50]
        self.ack = 0

    def send_data(self, sender_id, receiver_id, data, piggyback_ack):
        """Send data from sender to receiver with optional piggybacked acknowledgment"""
        message = f"Sender {sender_id} sends data {data} to Receiver {receiver_id}"
        if piggyback_ack:
            message += " (with piggybacked ACK)"
        print(message)
    
    def receive_data(self, receiver_id, data, ack):
        """Receive data and send acknowledgment"""
        print(f"Receiver {receiver_id} received data {data} and sends ACK {ack}")

    def run_simulation(self):
        """Simulate piggybacking protocol with sample data"""
        print("\nStarting Piggybacking Protocol Simulation...")
        print("-------------------------------------------")
        
        for i, packet in enumerate(self.data_packets):
            # Send data with piggybacked ACK (except for first packet)
            piggyback_ack = (i > 0)
            self.send_data(1, 2, packet, piggyback_ack)
            
            # Simulate network delay
            time.sleep(1)
            
            # Receive data and acknowledge
            self.receive_data(2, packet, self.ack)
            self.ack += 1
            
            print("-------------------------------------------")
            
        print("Simulation Complete.\n")

if __name__ == "__main__":
    protocol = PiggybackProtocol()
    protocol.run_simulation()
