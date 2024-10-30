from pow_blockchain import Pow_Blockchain, Block
from pos_blockchain import PoSBlockchain, PosBlock
import time

def test_pow_pos():
    # Test Proof of Work
    pow_blockchain = Pow_Blockchain()
    pow_start_time = time.time()
    pow_blockchain.add_block(Block(1, "", int(time.time()), "Transaction Data 1"))
    pow_blockchain.add_block(Block(2, "", int(time.time()), "Transaction Data 2"))
    pow_blockchain.add_block(Block(3, "", int(time.time()), "Transaction Data 3"))
    pow_end_time = time.time()
    pow_execution_time = pow_end_time - pow_start_time

    # Test Proof of Stake
    pos_blockchain = PoSBlockchain(100)
    pos_start_time = time.time()
    pos_blockchain.add_block(PosBlock(1, "", int(time.time()), "Transaction Data 1", 100, "Validator A"))
    pos_blockchain.add_block(PosBlock(2, "", int(time.time()), "Transaction Data 2", 150, "Validator B"))
    pos_blockchain.add_block(PosBlock(3, "", int(time.time()), "Transaction Data 3", 75, "Validator C"))
    pos_end_time = time.time()
    pos_execution_time = pos_end_time - pos_start_time

    print(f"Proof of Work Execution Time: {pow_execution_time * 1000:.6f} milliseconds")
    print(f"Proof of Stake Execution Time: {pos_execution_time * 1000:.6f} milliseconds")

    if pow_execution_time < pos_execution_time:
        print("Proof of Work is faster than Proof of Stake")
    else:
        print("Proof of Stake is faster than Proof of Work")

if __name__ == "__main__":
    test_pow_pos()