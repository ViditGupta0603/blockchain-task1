import hashlib
import time

class Block:
    def __init__(self, data):
        self.data = data
        self.nonce = 0
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = f"{self.data}{self.nonce}{self.timestamp}" # Combine data, nonce, and timestamp to use .encode()
        # to ensure the string is in bytes format for hashing
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        attempts = 0
        start_time = time.time()

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        end_time = time.time()
        print(f"Block mined! Hash: {self.hash}")
        print(f"Nonce attempts: {attempts}")
        print(f"Time taken: {end_time - start_time:.4f} seconds")

# -----------------------------
# 🔧 Usage Example
difficulty = 4  # hash must start with "0000"
block = Block("Simulating PoW mining...")
block.mine_block(difficulty)
