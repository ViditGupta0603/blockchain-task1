import hashlib
import time

class Block:
    def __init__(self, index, data, previousHash=''):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def __str__(self):
        return (
            f"Block #{self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Data: {self.data}\n"
            f"Previous Hash: {self.previousHash}\n"
            f"Hash: {self.hash}\n"
            f"{'-'*40}"
        )

# 🧱 Create 3 linked blocks
blockchain = []

# Genesis block (first block)
genesis_block = Block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

# Block 1
block1 = Block(1, "First Block Data", genesis_block.hash)
blockchain.append(block1)

# Block 2
block2 = Block(2, "Second Block Data", block1.hash)
blockchain.append(block2)

# 🖨️ Display all blocks
print("\n Blockchain:")
for block in blockchain:
    print(block)

# 🔄 Challenge: Tamper with Block 1's data
print("\n Tampering with Block 1...")
block1.data = "Malicious Data"
block1.hash = block1.calculate_hash()

# Re-check integrity
print("\n Re-checking blockchain after tampering:")
for block in blockchain:
    print(block)

# ⛓️ Integrity check function
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        prev = chain[i - 1]

        if current.previousHash != prev.hash:
            print(f" Chain broken between Block {i-1} and Block {i}")
            return False

        if current.hash != current.calculate_hash():
            print(f" Block {i} has invalid hash.")
            return False

    print(" Blockchain is valid.")
    return True

# 🛡️ Run integrity check
print("\n Blockchain validity check:")
is_chain_valid(blockchain)
