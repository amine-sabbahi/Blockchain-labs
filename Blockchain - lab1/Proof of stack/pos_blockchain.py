import hashlib
import time

class PosBlock:
    def __init__(self, index, previous_hash, timestamp, data, stake_amount, validator_address):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.stake_amount = stake_amount
        self.validator_address = validator_address
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.stake_amount}{self.validator_address}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class PoSBlockchain:
    def __init__(self, min_stake):
        self.chain = [self.create_genesis_block()]
        self.min_stake = min_stake
        self.validators = {}

    def create_genesis_block(self):
        return PosBlock(0, "0", int(time.time()), "Genesis Block", 0, "Genesis Validator")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        self.update_validator_stakes(new_block.validator_address, new_block.stake_amount)

    def update_validator_stakes(self, validator_address, stake_amount):
        if validator_address in self.validators:
            self.validators[validator_address] += stake_amount
        else:
            self.validators[validator_address] = stake_amount

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            if self.validators[current_block.validator_address] < self.min_stake:
                return False

        return True

    def set_min_stake(self, min_stake):
        self.min_stake = min_stake

