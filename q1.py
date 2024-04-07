import time

class CovertChannel:
    def __init__(self):
        self.data = []

    def send(self, bit):
        self.data.append(bit)

    def receive(self):
        return self.data.pop(0) if self.data else None


if __name__ == "__main__":
    channel = CovertChannel()
    message = "1010101"  
    for bit in message:
        channel.send(bit)
        time.sleep(0.1)  
    received_message = ""
    bit = channel.receive()
    while bit:
        received_message += bit
        bit = channel.receive()
    print("Received Message:", received_message)
