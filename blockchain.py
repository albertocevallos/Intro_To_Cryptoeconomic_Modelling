## Step 1: Import Dependencies

# datetime library will generate the timestamps.
import datetime

# hashlib is a library contianing hashing algorithms.
import hashlib

## Step 2: Create a Block

 # Defining the 'Block' data structure, each 'block' has 7 attributes.
class Block:

    #1 Number of the block.
    blockNo = 0
    #2 What data is stored in the block (eg. BTC chain would contain transactions).
    data = None
    #3 Pointer to the next block.
    next = None
    #4 hash of this given block, also represent its unique ID and 
    # verifies the integrity of the blocks attributes (if they have changed or not).
    hash = None
    #5 Number only used once.
    nonce = 0
    #6 Stores the hash (ID) of the previous block in the chain.
    previous_hash = 0x0
    #7 Contains timestamp of when this block was generated.
    timestamp = datetime.datetime.now()

    # The init function will generate a block once data is stored in it.
    def __init__(self, data):
        self.data = data

    # This function contains the logic and algorithm to compute the 'hash' of a block.
    # A hash contains a unique ID of the attributes of the 'block', including
    # set of transactions, previous block hash, nonce and timestamp.
    # This feature makes the block (Aand its content) immutable.

    # If somone changes the a transaction then this will change the hash of the 'block'
    # and every block after would change. Why? Because hash functions are deterministic.
    def hash(self):
        # SHA-256 is a hashing algorithm that generates an almost-unique 256-bit signature
        # that represents some piece of text.
        h = hashlib.sha256()
        # The input to the SHA-256 algorithm will be a concatenated string consisting 
        # of 5 block attributes the nonce, data, previous hash, timestamp, & block number.
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        # Returns a hexademical string.
        return h.hexdigest()

    def __str__(self):
        # Print out the value of a block
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"    

## Step 3: Create a Blockchain

# Let's define the blockchain datastructure itsel. It will consist of 'blocks' linked
# together to form a chain.

class Blockchain:

    # Mining difficulty, dictates how computationally rigorous it is to mine a block
    diff = 20
    # Maximum number we can store in a 32-bit number
    maxNonce = 2**32
    # Target hash, for mining 
    target = 2 ** (256-diff)

    # Creates the first block in the blockchain ('Genesis Block')
    block = Block("Genesis")
    # Sets the 'Genesis Block' as the head of the chain
    head = block

    # 'Add' function will add a given block to the chain of blocks. The block to be added
    # is the only parameter.
    def add(self, block):

        # Uses the hash (ID) of the last block in the chain 
        # as our new block's previous hash.
        block.previous_hash
        # Sets the block # of our new block as the last block's
        # number +1.
        block.blockNo = self.block.blockNo + 1

        # Sets the next (new) block equal to itself. This is the new head of the blockchain.
        self.block.next = block
        self.block = self.block.next

    # Defines a 'mining' function that determines where a given block
    # can be added to the blockchain or not.
    def mine(self, block):
        # From 0 to 2 ** 23
        for n in range(self.maxNonce):
            # Triggers mining of the block is the hash is less than the target value.
            if int(block.hash(), 16) <= self.target:
                # If it is smallerm then the block will be added
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

## Step 4: Print the Blockchain

# Initialize the blockchain.
blockchain = Blockchain()

# To mine 1o blocks, run the loop for 10x.
for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

# Prints out the content of each block in the blockchain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
