from hashlib import sha256
from datetime import datetime





class Block():
  def __init__(self, index, diff, data, previous_block_hash): #index represents the index of the block in the blockchain
    self.timestamp = datetime.utcnow()
    self.index = index
    self.data = data #for a cryptocurrency, this contains details about the transaction(eg: sender, receiver, amount transferred)
    self.prev_block_hash = previous_block_hash
    self.difficulty = diff # I am not using it in the calculation of the hash
    self.hash = self.calculate_valid_hash()

  def is_hash_valid(self, hash):
      return (hash.startswith('0' * (self.difficulty)))

  # Mining is required(as an implementation of proof of work) to make the process of adding new block to the blockchain slow and steady
  def calculate_valid_hash(self):
      print("Mining a new block with data: ", self.data)
      hash = ''
      nonce = 0
      while (not self.is_hash_valid(hash)):
          temp = self.to_string() + str(nonce)
          hash = sha256(temp.encode()).hexdigest()
          nonce += 1
      # self.hash = hash
      print("Mining completed")
      return hash

  def to_string(self):
    return "{0}\t{1}\t{2}\t{3}".format(self.index, self.data, self.timestamp, self.prev_block_hash)






####################################################################################################
class Blockchain():
    def __init__(self):
        self.chain =[]
        self.difficulty = 3 #4 takes a bit too much time
        self.set_genesis_block() 
        # As soon as we define a Blockchain object, its genesis block would be constructed by default
    
    def set_genesis_block(self):
        data = "Genesis\t"
        prev_hash = '0'*64
        genesis_block = Block(0, self.difficulty, data, prev_hash) #Index of genesis block: set to 0 (we are following 0 based indexing) 
        self.chain.append(genesis_block)
    
    def get_last_block(self):
        last_block = self.chain[-1]
        return last_block

    def get_last_hash(self):
        last_block = self.chain[-1]
        last_hash = last_block.hash
        return (last_hash)

    def get_last_index(self):
        last_block = self.chain[-1]
        last_index = last_block.index
        return (last_index)

    # Add the data(details about the transaction) in the blockchain as a new block
    def add_new_block(self, data):
        prev_hash = self.get_last_hash()
        prev_id = self.get_last_index()
        new_block = Block(prev_id+1, self.difficulty, data, prev_hash)
        self.chain.append(new_block)

    def get_blocks(self):
        return (self.chain)

    def print_block_chain(self):
      print("\n\n \t\t\t\t  <<<<<<<<<<<<<  Currently the block chain is as follows  >>>>>>>>>>>>>>")
      for block in self.chain:
        print()
        print('\t' + block.to_string())
        print()

    def is_valid_chain(self):
      for i in range(1, len(self.chain)):
        b1 = self.chain[i-1];
        b2 = self.chain[i];
        # if not b2.hasValidTransactions():
        #   print("error 3");
        #   return False;
        if b2.hash != b2.calculate_valid_hash():
          print("error 404");
          return False;

        if b2.prev_block_hash != b1.hash:
          print("error 504");
          return False;
      return True;
